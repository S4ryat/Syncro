import React, { useEffect, useState } from 'react';
import axios from 'axios';



const Recommendation = () => {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        // Récupérer les recommandations depuis votre backend lors du chargement de la page
        const fetchRecommendations = async () => {
            try {
                const response = await axios.get('/api/recommendations');
                setRecommendations(response.data);
            } catch (error) {
                console.error('Error fetching recommendations:', error);
            }
        };

        fetchRecommendations();
    }, []);

    return (
        <div>

            <h1>Recommendations</h1>
            <div className="recommendation-list">
                {recommendations.map((recommendation, index) => (
                    <div key={index} className="recommendation-item">
                        <img src={recommendation.image} alt={recommendation.title} />
                        <h2>{recommendation.title}</h2>
                        <p>{recommendation.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Recommendation;
