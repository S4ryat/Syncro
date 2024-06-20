import React, { useState } from 'react';
import { FaRegUser } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const Profile = () => {
    const [file, setFile] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const [username, setUsername] = useState('');
    const [newUsername, setNewUsername] = useState('');
    const [bio, setBio] = useState('');
    const [newBio, setNewBio] = useState('');
    const [favoriteAlbums] = useState(['Album 1', 'Album 2', 'Album 3']);
    const [favoriteArtists] = useState(['Artiste 1', 'Artiste 2', 'Artiste 3']);
    const [favoritePlaylists] = useState(['Playlist 1', 'Playlist 2', 'Playlist 3']);
    const [usernameFocused, setUsernameFocused] = useState(false);
    const [bioFocused, setBioFocused] = useState(false);

    const handleFocus = (setter) => () => setter(true);
    const handleBlur = (setter, value) => () => {
        if (value.trim() === '') {
            setter(false);
        }
    };

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onloadend = () => {
            setFile(reader.result);
        };

        if (file) {
            reader.readAsDataURL(file);
        }
    };

    const handleEditClick = () => {
        setIsEditing(true);
    };

    const handleSaveClick = () => {
        setUsername(newUsername);
        setBio(newBio);
        setIsEditing(false);
    };

    const styles = {
        container: {
            fontFamily: 'Arial, sans-serif',
            backgroundColor: 'black',
            color: 'white',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100vh',
            margin: 0,
            position: 'relative',
        },
        profileContainer: {
            position: 'relative',
            maxWidth: '100%',
            width: '1000px',
            margin: '0 auto',
            backgroundColor: '#1E1E1E',
            borderRadius: '20px',
            boxShadow: '0 10px 30px rgba(0, 0, 0, 0.3)',
            padding: '20px',
            boxSizing: 'border-box',
        },
        header: {
            textAlign: 'center',
            marginBottom: '20px',
        },
        headerTitle: {
            fontSize: 'clamp(2em, 5vw, 3em)',
            color: '#0ef',
            marginBottom: '10px',
        },
        cardImg: {
            width: '100%',
            height: '200px',
            background: '#333',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            position: 'relative',
            borderRadius: '10px',
            overflow: 'hidden',
        },
        cardAvatar: {
            width: '120px',
            height: '120px',
            borderRadius: '50%',
            backgroundColor: 'black',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            cursor: 'pointer',
            zIndex: 1,
        },
        cardAvatarImg: {
            width: '110px',
            height: '110px',
            borderRadius: '50%',
            objectFit: 'cover',
        },
        inputFile: {
            display: 'none',
        },
        editButton: {
            marginTop: '10px',
            padding: '10px 20px',
            fontSize: '16px',
            cursor: 'pointer',
            borderRadius: '5px',
            border: 'none',
            backgroundColor: '#0ef',
            color: '#121212',
            transition: 'background-color 0.3s ease',
        },
        input: {
            marginTop: '10px',
            marginBottom: '20px',
            padding: '10px',
            fontSize: '16px',
            borderRadius: '5px',
            border: '1px solid #e1e1e1',
            width: 'calc(100% - 22px)',
            backgroundColor: '#282828',
            color: '#ffffff',
            outline: 'none',
        },
        textarea: {
            marginTop: '10px',
            marginBottom: '20px',
            padding: '10px',
            fontSize: '16px',
            borderRadius: '5px',
            border: '1px solid #e1e1e1',
            width: 'calc(100% - 22px)',
            height: '100px',
            backgroundColor: '#282828',
            color: '#ffffff',
            resize: 'vertical',
            outline: 'none',
        },
        sectionTitle: {
            fontSize: 'clamp(1.2em, 3vw, 1.8em)',
            marginTop: '30px',
            marginBottom: '15px',
            color: '#0ef',
            borderBottom: '2px solid #0ef',
            paddingBottom: '10px',
        },
        list: {
            listStyleType: 'none',
            padding: 0,
        },
        listItem: {
            backgroundColor: '#282828',
            marginBottom: '10px',
            padding: '15px',
            borderRadius: '10px',
            transition: 'background-color 0.3s ease',
        },
        formContainer: {
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            display: 'flex',
            flexDirection: 'column',
            gap: '20px',
            color: 'white',
            width: '500px',
            maxWidth: '100%',
            padding: '20px',
            borderRadius: '10px',
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            boxShadow: '0 0 20px rgba(255, 255, 255, 0.1)',
            zIndex: 2,
        },
        formLabel: {
            fontSize: '15px',
            paddingLeft: '10px',
            position: 'absolute',
            left: '7px',
            transition: 'transform 0.3s ease, font-size 0.3s ease, color 0.3s ease',
            pointerEvents: 'none',
            color: '#ffffff',
        },
        formInput: {
            width: '100%',
            height: '45px',
            border: 'none',
            outline: 'none',
            padding: '0px 7px',
            borderRadius: '6px',
            color: '#fff',
            fontSize: '15px',
            backgroundColor: '#282828',
            boxShadow: '3px 3px 10px rgba(0, 0, 0, 1), -1px -1px 6px rgba(255, 255, 255, 0.4)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
        },
        bioInput: {
            height: '90px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'left',
        },
        labelFocused: {
            transform: 'translateY(-30px)',
            fontSize: '12px',
            color: '#0ef',
        },
    };


    return (
        <div style={styles.container}>
            <div style={styles.profileContainer}>
                <div style={styles.header}>
                    <h1 style={styles.headerTitle}>{username}</h1>
                </div>

                <div style={styles.cardImg}>
                    <input
                        type="file"
                        accept="image/*"
                        style={styles.inputFile}
                        id="imageUpload"
                        onChange={handleImageUpload}
                    />
                    <label htmlFor="imageUpload" style={styles.cardAvatar}>
                        {file ? (
                            <img src={file} alt="Profile" style={styles.cardAvatarImg} />
                        ) : (
                            <FaRegUser size={60} color="#ffffff" />
                        )}
                    </label>
                </div>

                {/* <p style={styles.input}>{bio}</p> */}

                {isEditing ? (
                    <div style={styles.formContainer}>
                        <div style={{ position: 'relative' }}>
                            <input
                                required
                                type="text"
                                name="username"
                                className="input"
                                value={newUsername}
                                onChange={(e) => setNewUsername(e.target.value)}
                                onFocus={handleFocus(setUsernameFocused)}
                                onBlur={handleBlur(setUsernameFocused, newUsername)}
                                style={styles.formInput}
                            />
                            <label
                                className="label"
                                style={
                                    (usernameFocused || newUsername) ?
                                        { ...styles.formLabel, ...styles.labelFocused } :
                                        styles.formLabel
                                }
                            >
                                Username
                            </label>
                        </div>
                        <div style={{ position: 'relative' }}>
                            <textarea
                                required
                                name="bio"
                                className="input bio-input"
                                value={newBio}
                                onChange={(e) => setNewBio(e.target.value)}
                                onFocus={handleFocus(setBioFocused)}
                                onBlur={handleBlur(setBioFocused, newBio)}
                                style={{ ...styles.formInput, ...styles.bioInput }}
                            />
                            <label
                                className="label"
                                style={
                                    (bioFocused || newBio) ?
                                        { ...styles.formLabel, ...styles.labelFocused } :
                                        styles.formLabel
                                }
                            >
                                Bio
                            </label>
                        </div>
                        <button onClick={handleSaveClick} style={styles.editButton}>Save</button>
                    </div>
                ) : (
                    <button onClick={handleEditClick} style={styles.editButton}>Edit Profile</button>
                )}
                <Link to="/favorites" style={styles.favoritesLink}>Voir mes favoris</Link>
                <div style={styles.sectionTitle}>Favorite Artists</div>
                <ul style={styles.list}>
                    {favoriteArtists.map((artist, index) => (
                        <li key={index} style={styles.listItem}>{artist}</li>
                    ))}
                </ul>

                <div style={styles.sectionTitle}>Favorite Playlists</div>
                <ul style={styles.list}>
                    {favoritePlaylists.map((playlist, index) => (
                        <li key={index} style={styles.listItem}>{playlist}</li>
                    ))}
                </ul>
            </div>
        </div>
    );

};

export default Profile;
