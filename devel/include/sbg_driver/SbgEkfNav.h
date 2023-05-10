// Generated by gencpp from file sbg_driver/SbgEkfNav.msg
// DO NOT EDIT!


#ifndef SBG_DRIVER_MESSAGE_SBGEKFNAV_H
#define SBG_DRIVER_MESSAGE_SBGEKFNAV_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>
#include <sbg_driver/SbgEkfStatus.h>

namespace sbg_driver
{
template <class ContainerAllocator>
struct SbgEkfNav_
{
  typedef SbgEkfNav_<ContainerAllocator> Type;

  SbgEkfNav_()
    : header()
    , time_stamp(0)
    , velocity()
    , velocity_accuracy()
    , latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)
    , undulation(0.0)
    , position_accuracy()
    , status()  {
    }
  SbgEkfNav_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , time_stamp(0)
    , velocity(_alloc)
    , velocity_accuracy(_alloc)
    , latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)
    , undulation(0.0)
    , position_accuracy(_alloc)
    , status(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _time_stamp_type;
  _time_stamp_type time_stamp;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _velocity_type;
  _velocity_type velocity;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _velocity_accuracy_type;
  _velocity_accuracy_type velocity_accuracy;

   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef double _altitude_type;
  _altitude_type altitude;

   typedef float _undulation_type;
  _undulation_type undulation;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _position_accuracy_type;
  _position_accuracy_type position_accuracy;

   typedef  ::sbg_driver::SbgEkfStatus_<ContainerAllocator>  _status_type;
  _status_type status;





  typedef boost::shared_ptr< ::sbg_driver::SbgEkfNav_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sbg_driver::SbgEkfNav_<ContainerAllocator> const> ConstPtr;

}; // struct SbgEkfNav_

typedef ::sbg_driver::SbgEkfNav_<std::allocator<void> > SbgEkfNav;

typedef boost::shared_ptr< ::sbg_driver::SbgEkfNav > SbgEkfNavPtr;
typedef boost::shared_ptr< ::sbg_driver::SbgEkfNav const> SbgEkfNavConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sbg_driver::SbgEkfNav_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sbg_driver::SbgEkfNav_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgEkfNav_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.time_stamp == rhs.time_stamp &&
    lhs.velocity == rhs.velocity &&
    lhs.velocity_accuracy == rhs.velocity_accuracy &&
    lhs.latitude == rhs.latitude &&
    lhs.longitude == rhs.longitude &&
    lhs.altitude == rhs.altitude &&
    lhs.undulation == rhs.undulation &&
    lhs.position_accuracy == rhs.position_accuracy &&
    lhs.status == rhs.status;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sbg_driver::SbgEkfNav_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgEkfNav_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sbg_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgEkfNav_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgEkfNav_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgEkfNav_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
{
  static const char* value()
  {
    return "16e5ed53c5544dda563fc67fb816d9b9";
  }

  static const char* value(const ::sbg_driver::SbgEkfNav_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x16e5ed53c5544ddaULL;
  static const uint64_t static_value2 = 0x563fc67fb816d9b9ULL;
};

template<class ContainerAllocator>
struct DataType< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sbg_driver/SbgEkfNav";
  }

  static const char* value(const ::sbg_driver::SbgEkfNav_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# SBG Ellipse Messages\n"
"\n"
"Header header\n"
"\n"
"# Time since sensor is powered up [us]\n"
"uint32 time_stamp\n"
"\n"
"# Velocity [m/s]\n"
"# In NED convention:\n"
"#   x: North\n"
"#   y: East\n"
"#   z: Down\n"
"# In ENU convention:\n"
"#   x: East\n"
"#   y: North\n"
"#   z: Up\n"
"geometry_msgs/Vector3 velocity\n"
"\n"
"# Velocity accuracy (1 sigma) [m/s].\n"
"# In NED convention:\n"
"#   x: North\n"
"#   y: East\n"
"#   z: Vertical\n"
"# In ENU convention:\n"
"#   x: East\n"
"#   y: North\n"
"#   z: Vertical\n"
"geometry_msgs/Vector3 velocity_accuracy\n"
"\n"
"# Latitude [degrees]. Positive is north of equator; negative is south\n"
"float64 latitude\n"
"\n"
"# Longitude [degrees]. Positive is east of prime meridian; negative is west\n"
"float64 longitude\n"
"\n"
"# Altitude [m]. Positive (above Mean Sea Level in meters)\n"
"float64 altitude\n"
"\n"
"# Altitude difference between the geoid and the Ellipsoid (WGS-84 Altitude - MSL Altitude)\n"
"# (Height above Ellipsoid = altitude + undulation) [m]\n"
"float32 undulation\n"
"\n"
"# Position accuracy (1 sigma) [m].\n"
"# In NED convention:\n"
"#   x: North\n"
"#   y: East\n"
"#   z: Vertical\n"
"# In ENU convention:\n"
"#   x: East\n"
"#   y: North\n"
"#   z: Vertical\n"
"geometry_msgs/Vector3 position_accuracy\n"
"\n"
"#  Global solution status\n"
"SbgEkfStatus status\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"================================================================================\n"
"MSG: sbg_driver/SbgEkfStatus\n"
"# SBG Ellipse Messages\n"
"# Submessage\n"
"\n"
"# Defines the Kalman filter computation mode (see the table 4 below)\n"
"# 0 UNINITIALIZED	The Kalman filter is not initialized and the returned data are all invalid.\n"
"# 1 VERTICAL_GYRO	The Kalman filter only rely on a vertical reference to compute roll and pitch angles. Heading and navigation data drift freely.\n"
"# 2 AHRS			A heading reference is available, the Kalman filter provides full orientation but navigation data drift freely.\n"
"# 3 NAV_VELOCITY	The Kalman filter computes orientation and velocity. Position is freely integrated from velocity estimation.\n"
"# 4 NAV_POSITION	Nominal mode, the Kalman filter computes all parameters (attitude, velocity, position). Absolute position is provided. \n"
"uint8 solution_mode \n"
"\n"
"# True if Attitude data is reliable (Roll/Pitch error < 0,5 deg)\n"
"bool attitude_valid\n"
"\n"
"# True if Heading data is reliable (Heading error < 1 deg)\n"
"bool heading_valid\n"
"\n"
"# True if Velocity data is reliable (velocity error < 1.5 m/s)\n"
"bool velocity_valid\n"
"\n"
"# True if Position data is reliable (Position error < 10m)\n"
"bool position_valid\n"
"\n"
"# True if vertical reference is used in solution (data used and valid since 3s)\n"
"bool vert_ref_used\n"
"\n"
"# True if magnetometer is used in solution (data used and valid since 3s)\n"
"bool mag_ref_used\n"
"\n"
"# True if GPS velocity is used in solution (data used and valid since 3s)\n"
"bool gps1_vel_used\n"
"\n"
"# True if GPS Position is used in solution (data used and valid since 3s)\n"
"bool gps1_pos_used\n"
"\n"
"# True if GPS Course is used in solution (data used and valid since 3s)\n"
"bool gps1_course_used\n"
"\n"
"# True if GPS True Heading is used in solution (data used and valid since 3s)\n"
"bool gps1_hdt_used\n"
"\n"
"# True if GPS2 velocity is used in solution (data used and valid since 3s)\n"
"bool gps2_vel_used\n"
"\n"
"# True if GPS2 Position is used in solution (data used and valid since 3s)\n"
"bool gps2_pos_used\n"
"\n"
"# True if GPS2 Course is used in solution (data used and valid since 3s)\n"
"bool gps2_course_used\n"
"\n"
"# True if GPS2 True Heading is used in solution (data used and valid since 3s)\n"
"bool gps2_hdt_used\n"
"\n"
"# True if Odometer is used in solution (data used and valid since 3s)\n"
"bool odo_used\n"
;
  }

  static const char* value(const ::sbg_driver::SbgEkfNav_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.time_stamp);
      stream.next(m.velocity);
      stream.next(m.velocity_accuracy);
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.altitude);
      stream.next(m.undulation);
      stream.next(m.position_accuracy);
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SbgEkfNav_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sbg_driver::SbgEkfNav_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sbg_driver::SbgEkfNav_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "time_stamp: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.time_stamp);
    s << indent << "velocity: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.velocity);
    s << indent << "velocity_accuracy: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.velocity_accuracy);
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "altitude: ";
    Printer<double>::stream(s, indent + "  ", v.altitude);
    s << indent << "undulation: ";
    Printer<float>::stream(s, indent + "  ", v.undulation);
    s << indent << "position_accuracy: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.position_accuracy);
    s << indent << "status: ";
    s << std::endl;
    Printer< ::sbg_driver::SbgEkfStatus_<ContainerAllocator> >::stream(s, indent + "  ", v.status);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SBG_DRIVER_MESSAGE_SBGEKFNAV_H
