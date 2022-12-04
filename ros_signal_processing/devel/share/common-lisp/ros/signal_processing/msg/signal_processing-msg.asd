
(cl:in-package :asdf)

(defsystem "signal_processing-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AudioInfo" :depends-on ("_package_AudioInfo"))
    (:file "_package_AudioInfo" :depends-on ("_package"))
  ))