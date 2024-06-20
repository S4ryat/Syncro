import React from 'react';
import PropTypes from 'prop-types';
import { FaPlay, FaPause, FaForward, FaBackward } from 'react-icons/fa';

const PlayerControls = ({ isPlaying, onPlayPause, onNext, onPrevious }) => {
                return (
                                <div>
                                                <div className="player-controls">
                                                                <button className="control-btn" onClick={onPrevious}>
                                                                                <FaBackward />
                                                                </button>
                                                                <button className="control-btn" onClick={onPlayPause}>
                                                                                {isPlaying ? <FaPause /> : <FaPlay />}
                                                                </button>
                                                                <button className="control-btn" onClick={onNext}>
                                                                                <FaForward />
                                                                </button>
                                                </div>

                                                <style>{`
        .player-controls {
          display: flex;
          justify-content: center;
          margin-top: 20px;
        }

        .control-btn {
          background-color: #333;
          color: #fff;
          border: none;
          border-radius: 50%;
          width: 40px;
          height: 40px;
          font-size: 18px;
          display: flex;
          justify-content: center;
          align-items: center;
          margin: 0 10px;
          cursor: pointer;
          transition: background-color 0.3s ease;
        }

        .control-btn:hover {
          background-color: #555;
        }
      `}</style>
                                </div>
                );
};

PlayerControls.propTypes = {
                isPlaying: PropTypes.bool.isRequired,
                onPlayPause: PropTypes.func.isRequired,
                onNext: PropTypes.func.isRequired,
                onPrevious: PropTypes.func.isRequired,
};

export default PlayerControls;