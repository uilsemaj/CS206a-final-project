// Auto-generated. Do not edit!

// (in-package signal_processing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class AudioInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.bpm = null;
      this.timestamp = null;
      this.top = null;
      this.bottom = null;
    }
    else {
      if (initObj.hasOwnProperty('bpm')) {
        this.bpm = initObj.bpm
      }
      else {
        this.bpm = 0;
      }
      if (initObj.hasOwnProperty('timestamp')) {
        this.timestamp = initObj.timestamp
      }
      else {
        this.timestamp = 0.0;
      }
      if (initObj.hasOwnProperty('top')) {
        this.top = initObj.top
      }
      else {
        this.top = 0;
      }
      if (initObj.hasOwnProperty('bottom')) {
        this.bottom = initObj.bottom
      }
      else {
        this.bottom = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AudioInfo
    // Serialize message field [bpm]
    bufferOffset = _serializer.uint32(obj.bpm, buffer, bufferOffset);
    // Serialize message field [timestamp]
    bufferOffset = _serializer.float64(obj.timestamp, buffer, bufferOffset);
    // Serialize message field [top]
    bufferOffset = _serializer.uint32(obj.top, buffer, bufferOffset);
    // Serialize message field [bottom]
    bufferOffset = _serializer.uint32(obj.bottom, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AudioInfo
    let len;
    let data = new AudioInfo(null);
    // Deserialize message field [bpm]
    data.bpm = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [timestamp]
    data.timestamp = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [top]
    data.top = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [bottom]
    data.bottom = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'signal_processing/AudioInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5368011d7b904165cf3a2294c5b63f30';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 bpm # Beats per minute
    float64 timestamp # Time at end of recording
    uint32 top # Top part of time signature, 4 by default
    uint32 bottom # Bottom part of time signature, 4 by default
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AudioInfo(null);
    if (msg.bpm !== undefined) {
      resolved.bpm = msg.bpm;
    }
    else {
      resolved.bpm = 0
    }

    if (msg.timestamp !== undefined) {
      resolved.timestamp = msg.timestamp;
    }
    else {
      resolved.timestamp = 0.0
    }

    if (msg.top !== undefined) {
      resolved.top = msg.top;
    }
    else {
      resolved.top = 0
    }

    if (msg.bottom !== undefined) {
      resolved.bottom = msg.bottom;
    }
    else {
      resolved.bottom = 0
    }

    return resolved;
    }
};

module.exports = AudioInfo;
