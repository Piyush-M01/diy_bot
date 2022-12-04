# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sbg_driver/SbgUtcTime.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sbg_driver.msg
import std_msgs.msg

class SbgUtcTime(genpy.Message):
  _md5sum = "89495f07708fa38e487b6509c4edabaa"
  _type = "sbg_driver/SbgUtcTime"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# SBG Ellipse Messages
Header header

# Time since sensor is powered up (us)
uint32 time_stamp

# General UTC time and clock sync status
SbgUtcTimeStatus clock_status

# Year
uint16 year

# Month in Year [1 ... 12]
uint8 month

# Day in Month [1 ... 31]
uint8 day

# Hour in day [0 ... 23]
uint8 hour

# Minute in hour [0 ... 59]
uint8 min

# Second in minute [0 ... 60], Note 60 is when a leap second is added.
uint8 sec

# Nanosecond of second.
uint32 nanosec

# GPS Time of week (ms)
uint32 gps_tow

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sbg_driver/SbgUtcTimeStatus
# SBG Ellipse Messages

# True when a clock input can be used to synchronize the internal clock.
bool clock_stable

# Define the internal clock estimation status
# 0 An error has occurred on the clock estimation.
# 1 The clock is only based on the internal crystal.
# 2 A PPS has been detected and the clock is converging to it.
# 3 The clock has converged to the PPS and is within 500ns.
uint8 clock_status

# True if UTC time is synchronized with a PPS
bool clock_utc_sync

# UTC validity status
# 0 The UTC time is not known, we are just propagating the UTC time internally.
# 1 We have received valid UTC time information but we don't have the leap seconds information.
# 2 We have received valid UTC time data with valid leap seconds.
uint8 clock_utc_status"""
  __slots__ = ['header','time_stamp','clock_status','year','month','day','hour','min','sec','nanosec','gps_tow']
  _slot_types = ['std_msgs/Header','uint32','sbg_driver/SbgUtcTimeStatus','uint16','uint8','uint8','uint8','uint8','uint8','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,clock_status,year,month,day,hour,min,sec,nanosec,gps_tow

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SbgUtcTime, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.clock_status is None:
        self.clock_status = sbg_driver.msg.SbgUtcTimeStatus()
      if self.year is None:
        self.year = 0
      if self.month is None:
        self.month = 0
      if self.day is None:
        self.day = 0
      if self.hour is None:
        self.hour = 0
      if self.min is None:
        self.min = 0
      if self.sec is None:
        self.sec = 0
      if self.nanosec is None:
        self.nanosec = 0
      if self.gps_tow is None:
        self.gps_tow = 0
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.clock_status = sbg_driver.msg.SbgUtcTimeStatus()
      self.year = 0
      self.month = 0
      self.day = 0
      self.hour = 0
      self.min = 0
      self.sec = 0
      self.nanosec = 0
      self.gps_tow = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I4BH5B2I().pack(_x.time_stamp, _x.clock_status.clock_stable, _x.clock_status.clock_status, _x.clock_status.clock_utc_sync, _x.clock_status.clock_utc_status, _x.year, _x.month, _x.day, _x.hour, _x.min, _x.sec, _x.nanosec, _x.gps_tow))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.clock_status is None:
        self.clock_status = sbg_driver.msg.SbgUtcTimeStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 23
      (_x.time_stamp, _x.clock_status.clock_stable, _x.clock_status.clock_status, _x.clock_status.clock_utc_sync, _x.clock_status.clock_utc_status, _x.year, _x.month, _x.day, _x.hour, _x.min, _x.sec, _x.nanosec, _x.gps_tow,) = _get_struct_I4BH5B2I().unpack(str[start:end])
      self.clock_status.clock_stable = bool(self.clock_status.clock_stable)
      self.clock_status.clock_utc_sync = bool(self.clock_status.clock_utc_sync)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I4BH5B2I().pack(_x.time_stamp, _x.clock_status.clock_stable, _x.clock_status.clock_status, _x.clock_status.clock_utc_sync, _x.clock_status.clock_utc_status, _x.year, _x.month, _x.day, _x.hour, _x.min, _x.sec, _x.nanosec, _x.gps_tow))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.clock_status is None:
        self.clock_status = sbg_driver.msg.SbgUtcTimeStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 23
      (_x.time_stamp, _x.clock_status.clock_stable, _x.clock_status.clock_status, _x.clock_status.clock_utc_sync, _x.clock_status.clock_utc_status, _x.year, _x.month, _x.day, _x.hour, _x.min, _x.sec, _x.nanosec, _x.gps_tow,) = _get_struct_I4BH5B2I().unpack(str[start:end])
      self.clock_status.clock_stable = bool(self.clock_status.clock_stable)
      self.clock_status.clock_utc_sync = bool(self.clock_status.clock_utc_sync)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_I4BH5B2I = None
def _get_struct_I4BH5B2I():
    global _struct_I4BH5B2I
    if _struct_I4BH5B2I is None:
        _struct_I4BH5B2I = struct.Struct("<I4BH5B2I")
    return _struct_I4BH5B2I
