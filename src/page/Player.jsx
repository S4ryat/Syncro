import React, { useState, useEffect } from "react";
import PlayerControls from "../components/PlayerControls";
import PlayerDisplay from "../components/PlayerDisplay";
import VolumeControl from "../components/PlayerControls";

const Player = () => {
                const [currentSong, setCurrentSong] = useState(null);
                const [isPlaying, setIsPlaying] = useState(false);
                const [volume, setVolume] = useState(0.5);

                useEffect(() => {
                                // Exemple de chargement de la chanson
                                const fetchSong = async () => {
                                                const response = await fetch('/api/song');
                                                const songData = await response.json();
                                                setCurrentSong(songData);
                                };

                                fetchSong();
                }, []);

                const handlePlayPause = () => {
                                setIsPlaying(!isPlaying);
                };

                const handleNext = () => {
                                // Logic to go to the next song
                };

                const handlePrevious = () => {
                                // Logic to go to the previous song
                };

                const handleVolumeChange = (newVolume) => {
                                setVolume(newVolume);
                };

                return (
                                <div className="player">
                                                <PlayerDisplay song={currentSong} />
                                                <PlayerControls
                                                                isPlaying={isPlaying}
                                                                onPlayPause={handlePlayPause}
                                                                onNext={handleNext}
                                                                onPrevious={handlePrevious}
                                                />
                                                <VolumeControl
                                                                volume={volume}
                                                                onVolumeChange={handleVolumeChange}
                                                />

                                                <style>{`
        .player {
          display: flex;
          flex-direction: column;
          align-items: center;
          background-color: #f0f0f0;
          padding: 20px;
          border-radius: 10px;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
      `}</style>
                                </div>
                );
};

export default Player;