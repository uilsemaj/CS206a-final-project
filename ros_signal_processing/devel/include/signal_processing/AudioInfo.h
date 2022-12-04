// Generated by gencpp from file signal_processing/AudioInfo.msg
// DO NOT EDIT!


#ifndef SIGNAL_PROCESSING_MESSAGE_AUDIOINFO_H
#define SIGNAL_PROCESSING_MESSAGE_AUDIOINFO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace signal_processing
{
template <class ContainerAllocator>
struct AudioInfo_
{
  typedef AudioInfo_<ContainerAllocator> Type;

  AudioInfo_()
    : bpm(0)
    , timestamp(0.0)
    , top(0)
    , bottom(0)  {
    }
  AudioInfo_(const ContainerAllocator& _alloc)
    : bpm(0)
    , timestamp(0.0)
    , top(0)
    , bottom(0)  {
  (void)_alloc;
    }



   typedef uint32_t _bpm_type;
  _bpm_type bpm;

   typedef double _timestamp_type;
  _timestamp_type timestamp;

   typedef uint32_t _top_type;
  _top_type top;

   typedef uint32_t _bottom_type;
  _bottom_type bottom;





  typedef boost::shared_ptr< ::signal_processing::AudioInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::signal_processing::AudioInfo_<ContainerAllocator> const> ConstPtr;

}; // struct AudioInfo_

typedef ::signal_processing::AudioInfo_<std::allocator<void> > AudioInfo;

typedef boost::shared_ptr< ::signal_processing::AudioInfo > AudioInfoPtr;
typedef boost::shared_ptr< ::signal_processing::AudioInfo const> AudioInfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::signal_processing::AudioInfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::signal_processing::AudioInfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::signal_processing::AudioInfo_<ContainerAllocator1> & lhs, const ::signal_processing::AudioInfo_<ContainerAllocator2> & rhs)
{
  return lhs.bpm == rhs.bpm &&
    lhs.timestamp == rhs.timestamp &&
    lhs.top == rhs.top &&
    lhs.bottom == rhs.bottom;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::signal_processing::AudioInfo_<ContainerAllocator1> & lhs, const ::signal_processing::AudioInfo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace signal_processing

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::signal_processing::AudioInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::signal_processing::AudioInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::signal_processing::AudioInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::signal_processing::AudioInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::signal_processing::AudioInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::signal_processing::AudioInfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::signal_processing::AudioInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5368011d7b904165cf3a2294c5b63f30";
  }

  static const char* value(const ::signal_processing::AudioInfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5368011d7b904165ULL;
  static const uint64_t static_value2 = 0xcf3a2294c5b63f30ULL;
};

template<class ContainerAllocator>
struct DataType< ::signal_processing::AudioInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "signal_processing/AudioInfo";
  }

  static const char* value(const ::signal_processing::AudioInfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::signal_processing::AudioInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32 bpm # Beats per minute\n"
"float64 timestamp # Time at end of recording\n"
"uint32 top # Top part of time signature, 4 by default\n"
"uint32 bottom # Bottom part of time signature, 4 by default\n"
;
  }

  static const char* value(const ::signal_processing::AudioInfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::signal_processing::AudioInfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.bpm);
      stream.next(m.timestamp);
      stream.next(m.top);
      stream.next(m.bottom);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AudioInfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::signal_processing::AudioInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::signal_processing::AudioInfo_<ContainerAllocator>& v)
  {
    s << indent << "bpm: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.bpm);
    s << indent << "timestamp: ";
    Printer<double>::stream(s, indent + "  ", v.timestamp);
    s << indent << "top: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.top);
    s << indent << "bottom: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.bottom);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIGNAL_PROCESSING_MESSAGE_AUDIOINFO_H
