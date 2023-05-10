# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sbg_driver/SbgGpsHdt.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SbgGpsHdt(genpy.Message):
  _md5sum = "8c984f2f80abb760d3b4701ef29aeceb"
  _type = "sbg_driver/SbgGpsHdt"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# SBG Ellipse Messages
Header header

# Time since sensor is powered up [us]
uint32 time_stamp

# GPS True Heading status.
# Bit 0-5: enum:
# 0 SOL_COMPUTED		A valid solution has been computed.
# 1 INSUFFICIENT_OBS	Not enough valid SV to compute a solution.
# 2 INTERNAL_ERROR		An internal error has occurred.
# 3 HEIGHT_LIMIT		The height limit has been exceeded.
# Bit 6: mask:
# 1 BASELINE_VALID      The baseline length field is filled and valid.
uint16 status

# GPS Time of Week [ms]
uint32 tow

# True heading angle (0 to 360 deg)
# NED convention: Rotation about the down axis. Zero when the X axis is pointing North.
# ENU convention: Rotation about the up axis. Zero when the X axis is pointing East. (opposite sign compared to NED)
float32 true_heading

# 1 sigma True heading estimated accuracy
float32 true_heading_acc

# Pitch
# NED convention:
#   angle from the master to the rover
# ENU convention:
#   angle from the rover to the master
float32 pitch

# 1 sigma pitch estimated accuracy
float32 pitch_acc

# The distance between the main and aux antenna in meters.
float32 baseline

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
"""
  __slots__ = ['header','time_stamp','status','tow','true_heading','true_heading_acc','pitch','pitch_acc','baseline']
  _slot_types = ['std_msgs/Header','uint32','uint16','uint32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,status,tow,true_heading,true_heading_acc,pitch,pitch_acc,baseline

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SbgGpsHdt, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.status is None:
        self.status = 0
      if self.tow is None:
        self.tow = 0
      if self.true_heading is None:
        self.true_heading = 0.
      if self.true_heading_acc is None:
        self.true_heading_acc = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.pitch_acc is None:
        self.pitch_acc = 0.
      if self.baseline is None:
        self.baseline = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.status = 0
      self.tow = 0
      self.true_heading = 0.
      self.true_heading_acc = 0.
      self.pitch = 0.
      self.pitch_acc = 0.
      self.baseline = 0.

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
      buff.write(_get_struct_IHI5f().pack(_x.time_stamp, _x.status, _x.tow, _x.true_heading, _x.true_heading_acc, _x.pitch, _x.pitch_acc, _x.baseline))
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
      end += 30
      (_x.time_stamp, _x.status, _x.tow, _x.true_heading, _x.true_heading_acc, _x.pitch, _x.pitch_acc, _x.baseline,) = _get_struct_IHI5f().unpack(str[start:end])
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
      buff.write(_get_struct_IHI5f().pack(_x.time_stamp, _x.status, _x.tow, _x.true_heading, _x.true_heading_acc, _x.pitch, _x.pitch_acc, _x.baseline))
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
      end += 30
      (_x.time_stamp, _x.status, _x.tow, _x.true_heading, _x.true_heading_acc, _x.pitch, _x.pitch_acc, _x.baseline,) = _get_struct_IHI5f().unpack(str[start:end])
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
_struct_IHI5f = None
def _get_struct_IHI5f():
    global _struct_IHI5f
    if _struct_IHI5f is None:
        _struct_IHI5f = struct.Struct("<IHI5f")
    return _struct_IHI5f
