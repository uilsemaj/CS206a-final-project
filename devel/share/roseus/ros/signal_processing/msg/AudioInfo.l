;; Auto-generated. Do not edit!


(when (boundp 'signal_processing::AudioInfo)
  (if (not (find-package "SIGNAL_PROCESSING"))
    (make-package "SIGNAL_PROCESSING"))
  (shadow 'AudioInfo (find-package "SIGNAL_PROCESSING")))
(unless (find-package "SIGNAL_PROCESSING::AUDIOINFO")
  (make-package "SIGNAL_PROCESSING::AUDIOINFO"))

(in-package "ROS")
;;//! \htmlinclude AudioInfo.msg.html


(defclass signal_processing::AudioInfo
  :super ros::object
  :slots (_bpm _timestamp _top _bottom ))

(defmethod signal_processing::AudioInfo
  (:init
   (&key
    ((:bpm __bpm) 0)
    ((:timestamp __timestamp) 0.0)
    ((:top __top) 0)
    ((:bottom __bottom) 0)
    )
   (send-super :init)
   (setq _bpm (round __bpm))
   (setq _timestamp (float __timestamp))
   (setq _top (round __top))
   (setq _bottom (round __bottom))
   self)
  (:bpm
   (&optional __bpm)
   (if __bpm (setq _bpm __bpm)) _bpm)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:top
   (&optional __top)
   (if __top (setq _top __top)) _top)
  (:bottom
   (&optional __bottom)
   (if __bottom (setq _bottom __bottom)) _bottom)
  (:serialization-length
   ()
   (+
    ;; uint32 _bpm
    4
    ;; float64 _timestamp
    8
    ;; uint32 _top
    4
    ;; uint32 _bottom
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _bpm
       (write-long _bpm s)
     ;; float64 _timestamp
       (sys::poke _timestamp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint32 _top
       (write-long _top s)
     ;; uint32 _bottom
       (write-long _bottom s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _bpm
     (setq _bpm (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _timestamp
     (setq _timestamp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint32 _top
     (setq _top (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _bottom
     (setq _bottom (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get signal_processing::AudioInfo :md5sum-) "5368011d7b904165cf3a2294c5b63f30")
(setf (get signal_processing::AudioInfo :datatype-) "signal_processing/AudioInfo")
(setf (get signal_processing::AudioInfo :definition-)
      "uint32 bpm # Beats per minute
float64 timestamp # Time at end of recording
uint32 top # Top part of time signature, 4 by default
uint32 bottom # Bottom part of time signature, 4 by default

")



(provide :signal_processing/AudioInfo "5368011d7b904165cf3a2294c5b63f30")


