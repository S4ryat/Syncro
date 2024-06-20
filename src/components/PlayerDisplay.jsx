import React from 'react';
import PropTypes from 'prop-types';

const PlayerDisplay = ({ song }) => {
                if (!song) {
                                return <div className="loading">Loading...</div>;
                }

                const { title, artist, album, cover } = song;

                return (
                                <div>
                                                <div className="player-display">
                                                                <div className="cover">
                                                                                <img src={cover} alt={`${title} cover`} />
                                                                </div>
                                                                <div className="info">
                                                                                <h2>{title}</h2>
                                                                                <h3>{artist}</h3>
                                                                                <p>{album}</p>
                                                                </div>
                                                </div>

                                                <style>{`
        .player-display {
          display: flex;
          align-items: center;
          margin-bottom: 20px;
        }

        .cover {
          width: 150px;
          height: 150px;
          overflow: hidden;
          border-radius: 10px;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .cover img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        .info {
          margin-left: 20px;
        }

        .info h2 {
          font-size: 24px;
          margin-bottom: 5px;
        }

        .info h3 {
          font-size: 18px;
          color: #666;
          margin-bottom: 5px;
        }

        .info p {
          font-size: 16px;
          color: #888;
        }

        .loading {
          font-size: 18px;
          color: #666;
        }
      `}</style>
                                </div>
                );
};

PlayerDisplay.propTypes = {
                song: PropTypes.shape({
                                title: PropTypes.string.isRequired,
                                artist: PropTypes.string.isRequired,
                                album: PropTypes.string.isRequired,
                                cover: PropTypes.string.isRequired,
                }),
};

export default PlayerDisplay;