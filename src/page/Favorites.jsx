import React from 'react';
import Playlist from './Playlist';
import { Link } from 'react-router-dom';

const Favorites = () => {
                const styles = {
                                body: {
                                                fontFamily: 'Arial, sans-serif',
                                                backgroundColor: '#121212',
                                                color: 'white',
                                                margin: 0,
                                                padding: 0,
                                                display: 'flex',
                                                flexDirection: 'column',
                                                alignItems: 'flex-start',
                                                minHeight: '100vh',  // Utilisation de 100vh pour la hauteur
                                                width: '100vw',      // Utilisation de 100vw pour la largeur
                                                marginLeft: '0',
                                                minHeight: '100vh',  // Utilisation de 100vh pour la hauteur
                                                width: '100vw',      // Utilisation de 100vw pour la largeur
                                                overflow: 'hidden',  // Empêche le scroll dans le body
                                },
                                header: {
                                                display: 'flex',
                                                alignItems: 'center',
                                                justifyContent: 'flex-start',
                                                marginTop: '20px',
                                                width: '80%',
                                                paddingLeft: '20px',

                                },
                                heart: {
                                                fontSize: '80px',
                                                color: 'red',
                                                marginRight: '20px',
                                },
                                title: {
                                                fontSize: '40px',
                                                fontWeight: 'bold',
                                                marginRight: '20px',
                                },
                                userInfo: {
                                                textAlign: 'left',
                                                marginTop: '10px',
                                                width: '80%',
                                                paddingLeft: '20px',
                                                marginLeft: '130px',
                                },
                                username: {
                                                fontSize: '24px',
                                                marginBottom: '5px',
                                },
                                likedCount: {
                                                fontSize: '18px',
                                                color: '#ccc',
                                },
                                listTitle: {
                                                fontSize: '28px',
                                                marginTop: '20px',
                                                width: '80%',
                                                paddingLeft: '20px',
                                                marginLeft: '130px',
                                                marginBottom: '30px'
                                },
                                listHeader: {
                                                display: 'flex',
                                                justifyContent: 'space-between',
                                                width: '80%',
                                                marginTop: '10px',
                                                fontSize: '18px',
                                                paddingBottom: '5px',
                                                borderBottom: '1px solid #444',
                                                paddingLeft: '20px',
                                                marginLeft: '130px',
                                },
                                listItem: {
                                                display: 'flex',
                                                justifyContent: 'space-between',
                                                width: '80%',
                                                padding: '10px 0',
                                                marginBottom: '10px',
                                                paddingLeft: '20px',
                                                marginLeft: '130px',
                                },
                                index: {
                                                width: '5%',
                                },
                                itemTitle: {
                                                width: '30%',
                                },
                                itemAlbum: {
                                                width: '30%',
                                },
                                itemDateAdded: {
                                                width: '25%',
                                },
                                itemDuration: {
                                                width: '15%',
                                },
                };

                const likedSongs = [
                                { id: 1, title: 'Titre 1', album: 'Album 1', dateAdded: '01/01/2023', duration: '3:45' },
                                { id: 2, title: 'Titre 2', album: 'Album 2', dateAdded: '02/02/2023', duration: '4:00' },
                                { id: 3, title: 'Titre 3', album: 'Album 3', dateAdded: '03/03/2023', duration: '2:30' },
                ];

                return (
                                <div style={styles.body}>
                                                <div style={styles.header}>
                                                                <div className="heart" style={styles.heart}>❤️</div>
                                                                <div className="title" style={styles.title}>Favoris</div>
                                                </div>
                                                <div style={styles.userInfo} className="user-info">
                                                                <div className="username" style={styles.username}>Nom d'utilisateur</div>
                                                                <div className="liked-count" style={styles.likedCount}>10 titres likés</div>
                                                </div>
                                                <div style={styles.listTitle} className="list-title">Titres Likés</div>
                                                <div style={styles.listHeader} className="list-header">
                                                                <div className="index" style={styles.index}>#</div>
                                                                <div className="title" style={styles.itemTitle}>Titre</div>
                                                                <div className="album" style={styles.itemAlbum}>Album</div>
                                                                <div className="date-added" style={styles.itemDateAdded}>Date d'ajout</div>
                                                                <div className="duration" style={styles.itemDuration}>Durée</div>
                                                </div>
                                                {likedSongs.map((song, index) => (
                                                                <div key={song.id} style={styles.listItem} className="list-item">
                                                                                <div className="index" style={styles.index}>{index + 1}</div>
                                                                                <div className="title" style={styles.itemTitle}>{song.title}</div>
                                                                                <div className="album" style={styles.itemAlbum}>{song.album}</div>
                                                                                <div className="date-added" style={styles.itemDateAdded}>{song.dateAdded}</div>
                                                                                <div className="duration" style={styles.itemDuration}>{song.duration}</div>
                                                                </div>
                                                ))}
                                                <Link to="/playlist">Playlist</Link>
                                </div>
                );
};

export default Favorites;
