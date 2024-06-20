import React from 'react';
import PropTypes from 'prop-types';

const VolumeControl = ({ volume, onVolumeChange }) => {
                return (
                                <div>
                                                <div className="volume-control">
                                                                <input
                                                                                type="range"
                                                                                min="0"
                                                                                max="1"
                                                                                step="0.01"
                                                                                value={volume}
                                                                                onChange={(e) => onVolumeChange(e.target.value)}
                                                                />
                                                </div>

                                                <style>{`
        .volume-control {
          margin-top: 20px;
        }

        .volume-control input[type="range"] {
          width: 200px;
          height: 20px;
          background-color: #ddd;
          border-radius: 10px;
          outline: none;
          -webkit-appearance: none;
        }

        .volume-control input[type="range"]::-webkit-slider-thumb {
          -webkit-appearance: none;
          appearance: none;
          width: 15px;
          height: 15px;
          background-color: #333;
          border-radius: 50%;
          cursor: pointer;
        }
      `}</style>
                                </div>
                );
};

VolumeControl.propTypes = {
                volume: PropTypes.number.isRequired,
                onVolumeChange: PropTypes.func.isRequired,
};

export default VolumeControl;