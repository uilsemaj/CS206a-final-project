; Auto-generated. Do not edit!


(cl:in-package signal_processing-msg)


;//! \htmlinclude AudioInfo.msg.html

(cl:defclass <AudioInfo> (roslisp-msg-protocol:ros-message)
  ((bpm
    :reader bpm
    :initarg :bpm
    :type cl:integer
    :initform 0)
   (timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:float
    :initform 0.0)
   (top
    :reader top
    :initarg :top
    :type cl:integer
    :initform 0)
   (bottom
    :reader bottom
    :initarg :bottom
    :type cl:integer
    :initform 0))
)

(cl:defclass AudioInfo (<AudioInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AudioInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AudioInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name signal_processing-msg:<AudioInfo> is deprecated: use signal_processing-msg:AudioInfo instead.")))

(cl:ensure-generic-function 'bpm-val :lambda-list '(m))
(cl:defmethod bpm-val ((m <AudioInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader signal_processing-msg:bpm-val is deprecated.  Use signal_processing-msg:bpm instead.")
  (bpm m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <AudioInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader signal_processing-msg:timestamp-val is deprecated.  Use signal_processing-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'top-val :lambda-list '(m))
(cl:defmethod top-val ((m <AudioInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader signal_processing-msg:top-val is deprecated.  Use signal_processing-msg:top instead.")
  (top m))

(cl:ensure-generic-function 'bottom-val :lambda-list '(m))
(cl:defmethod bottom-val ((m <AudioInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader signal_processing-msg:bottom-val is deprecated.  Use signal_processing-msg:bottom instead.")
  (bottom m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AudioInfo>) ostream)
  "Serializes a message object of type '<AudioInfo>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bpm)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bpm)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'bpm)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'bpm)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'timestamp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'top)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'top)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'top)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'top)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bottom)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bottom)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'bottom)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'bottom)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AudioInfo>) istream)
  "Deserializes a message object of type '<AudioInfo>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bpm)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bpm)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'bpm)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'bpm)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'timestamp) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'top)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'top)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'top)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'top)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bottom)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bottom)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'bottom)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'bottom)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AudioInfo>)))
  "Returns string type for a message object of type '<AudioInfo>"
  "signal_processing/AudioInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AudioInfo)))
  "Returns string type for a message object of type 'AudioInfo"
  "signal_processing/AudioInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AudioInfo>)))
  "Returns md5sum for a message object of type '<AudioInfo>"
  "5368011d7b904165cf3a2294c5b63f30")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AudioInfo)))
  "Returns md5sum for a message object of type 'AudioInfo"
  "5368011d7b904165cf3a2294c5b63f30")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AudioInfo>)))
  "Returns full string definition for message of type '<AudioInfo>"
  (cl:format cl:nil "uint32 bpm # Beats per minute~%float64 timestamp # Time at end of recording~%uint32 top # Top part of time signature, 4 by default~%uint32 bottom # Bottom part of time signature, 4 by default~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AudioInfo)))
  "Returns full string definition for message of type 'AudioInfo"
  (cl:format cl:nil "uint32 bpm # Beats per minute~%float64 timestamp # Time at end of recording~%uint32 top # Top part of time signature, 4 by default~%uint32 bottom # Bottom part of time signature, 4 by default~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AudioInfo>))
  (cl:+ 0
     4
     8
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AudioInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'AudioInfo
    (cl:cons ':bpm (bpm msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':top (top msg))
    (cl:cons ':bottom (bottom msg))
))
