import React from 'react';
import PropTypes from 'prop-types';

const Playlist = ({ song }) => {
                const { title, artist, album, cover } = song;

                return (
                                <li className="playlist-item">
                                                <div className="cover">
                                                                <img src={cover} alt={`${title} cover`} />
                                                </div>
                                                <div className="info">
                                                                <h3>{title}</h3>
                                                                <p>{artist} - {album}</p>
                                                </div>

                                                <style>{`
        .playlist-item {
          display: flex;
          align-items: center;
          padding: 10px;
          background-color: #fff;
          border-radius: 4px;
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
          margin-bottom: 10px;
        }

        .cover {
          width: 50px;
          height: 50px;
          overflow: hidden;
          border-radius: 4px;
        }

        .cover img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        .info {
          margin-left: 10px;
        }

        .info h3 {
          margin: 0;
          font-size: 16px;
          color: #333;
        }

        .info p {
          margin: 0;
          font-size: 14px;
          color: #666;
        }
      `}</style>
                                </li>
                );
};

Playlist.propTypes = {
                song: PropTypes.shape({
                                title: PropTypes.string.isRequired,
                                artist: PropTypes.string.isRequired,
                                album: PropTypes.string.isRequired,
                                cover: PropTypes.string.isRequired,
                }).isRequired,
};

export default Playlist;