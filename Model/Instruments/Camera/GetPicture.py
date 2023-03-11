# Get picture
import datetime
from AtomImgSCNU.Model.Instruments.Camera.TUDefine import *
# OpenCamera
Path = '.AtomImgSCNU/Debug/'
TUCAM_Api_Init = TUSDKdll.TUCAM_Api_Init
TUCAMINIT = TUCAM_INIT(0, Path.encode('utf-8'))
TUCAM_Api_Init(pointer(TUCAMINIT));
#print(TUCAMINIT.uiCamCount)
#print(TUCAMINIT.pstrConfigPath)
TUCAM_Dev_Open = TUSDKdll.TUCAM_Dev_Open
TUCAMOPEN = TUCAM_OPEN(0, 0)
TUCAM_Dev_Open(pointer(TUCAMOPEN));
#print(TUCAMOPEN.uiIdxOpen)
#print(TUCAMOPEN.hIdxTUCam)

# Get Camera Info
TUCAM_Dev_GetInfo = TUSDKdll.TUCAM_Dev_GetInfo
# Camera name:
m_infoid = TUCAM_IDINFO
TUCAMVALUEINFO = TUCAM_VALUE_INFO(m_infoid.TUIDI_CAMERA_MODEL.value, 0, 0, 0)
TUCAM_Dev_GetInfo(c_int64(TUCAMOPEN.hIdxTUCam), pointer(TUCAMVALUEINFO))
#print(TUCAMVALUEINFO.pText)

# Camera VID
TUCAMVALUEINFO = TUCAM_VALUE_INFO(m_infoid.TUIDI_VENDOR.value, 0, 0, 0)
TUCAM_Dev_GetInfo(c_int64(TUCAMOPEN.hIdxTUCam), pointer(TUCAMVALUEINFO))
#print('%#X'%TUCAMVALUEINFO.nValue)

# Camera PID
TUCAMVALUEINFO = TUCAM_VALUE_INFO(m_infoid.TUIDI_PRODUCT.value, 0, 0, 0)
TUCAM_Dev_GetInfo(c_int64(TUCAMOPEN.hIdxTUCam), pointer(TUCAMVALUEINFO))
#print('%#X'%TUCAMVALUEINFO.nValue)

# Sdk API
TUCAMVALUEINFO = TUCAM_VALUE_INFO(m_infoid.TUIDI_VERSION_API.value, 0, 0, 0)
TUCAM_Dev_GetInfo(c_int64(TUCAMOPEN.hIdxTUCam), pointer(TUCAMVALUEINFO))
#print(TUCAMVALUEINFO.pText)

# FW
# TUCAMVALUEINFO = TUCAM_VALUE_INFO(m_infoid.TUIDI_VERSION_FRMW.value, 0, 0, 0)
# TUCAM_Dev_GetInfo(c_int64(TUCAMOPEN.hIdxTUCam), pointer(TUCAMVALUEINFO))
# if 0 == TUCAMVALUEINFO.nValue:
#     print(TUCAMVALUEINFO.pText)
# else:
#     print('%#X' % TUCAMVALUEINFO.nValue)

# SN
TUCAM_Reg_Read = TUSDKdll.TUCAM_Reg_Read
cSN = (c_char * 64)() 
pSN = cast(cSN, c_char_p)
TUCAMREGRW = TUCAM_REG_RW(1, pSN, 64)
TUCAM_Reg_Read(c_int64(TUCAMOPEN.hIdxTUCam), TUCAMREGRW)
#print(bytes(bytearray(cSN)))
#print(string_at(pSN))

# Save Image
m_frame = TUCAM_FRAME()
m_fs    = TUCAM_FILE_SAVE() 
m_format = TUIMG_FORMATS
m_frformat= TUFRM_FORMATS
m_capmode = TUCAM_CAPTURE_MODES

TUCAM_Buf_Alloc = TUSDKdll.TUCAM_Buf_Alloc
TUCAM_Cap_Start = TUSDKdll.TUCAM_Cap_Start
TUCAM_Buf_WaitForFrame = TUSDKdll.TUCAM_Buf_WaitForFrame
TUCAM_Buf_AbortWait = TUSDKdll.TUCAM_Buf_AbortWait
TUCAM_Cap_Stop = TUSDKdll.TUCAM_Cap_Stop
TUCAM_Buf_Release = TUSDKdll.TUCAM_Buf_Release
TUCAM_File_SaveImage = TUSDKdll.TUCAM_File_SaveImage
m_fs.nSaveFmt = m_format.TUFMT_TIF.value 

m_frame.pBuffer     = 0;
m_frame.ucFormatGet = m_frformat.TUFRM_FMT_RAW.value;
m_frame.uiRsdSize   = 1;         #需要获取的帧数，1                 
# print(m_frame.pBuffer)
# print(m_frame.ucFormatGet)

TUCAM_Buf_Alloc(c_int64(TUCAMOPEN.hIdxTUCam), pointer(m_frame))
#触发模式
TUCAM_Cap_Start(c_int64(TUCAMOPEN.hIdxTUCam), m_capmode.TUCCM_TRIGGER_STANDARD.value)
#from
#TUCAM_Cap_Start(c_int64(TUCAMOPEN.hIdxTUCam), m_capmode.TUCCM_SEQUENCE.value)

TUCAM_Buf_WaitForFrame(c_int64(TUCAMOPEN.hIdxTUCam), pointer(m_frame))
timestamp = datetime.datetime.now()
print(str(timestamp)[20:])
ImgName = './Image'+str(timestamp)[20:]
#ImgName = './Image'

m_fs.pFrame = pointer(m_frame);
m_fs.pstrSavePath = ImgName.encode('utf-8');
TUCAM_File_SaveImage(c_int64(TUCAMOPEN.hIdxTUCam), m_fs)
TUCAM_Buf_AbortWait(c_int64(TUCAMOPEN.hIdxTUCam));
TUCAM_Cap_Stop(c_int64(TUCAMOPEN.hIdxTUCam));
TUCAM_Buf_Release(c_int64(TUCAMOPEN.hIdxTUCam));

# CloseCamera
TUCAM_Dev_Close = TUSDKdll.TUCAM_Dev_Close
TUCAM_Dev_Close(c_int64(TUCAMOPEN.hIdxTUCam))
TUCAM_Api_Uninit = TUSDKdll.TUCAM_Api_Uninit
TUCAM_Api_Uninit

