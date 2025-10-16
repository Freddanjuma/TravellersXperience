// TravellersXperience - main.js
// Handles dynamic front-end features, API calls, and interactions

console.log("TravellersXperience main.js loaded successfully!");

// ========== API BASE CONFIG ==========
const API_BASE_URL = "http://127.0.0.1:8000/api"; // Change to your production URL later

// ========== AUTH HANDLERS ==========
async function registerUser(username, email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/register/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password })
        });
        const data = await response.json();
        console.log("User registered:", data);
        alert("Registration successful!");
    } catch (error) {
        console.error("Error registering user:", error);
        alert("Registration failed.");
    }
}

// ========== REVIEWS SECTION ==========
async function fetchReviews() {
    try {
        const response = await fetch(`${API_BASE_URL}/reviews/`);
        const reviews = await response.json();

        const container = document.getElementById("reviews-container");
        container.innerHTML = "";

        reviews.forEach(review => {
            const div = document.createElement("div");
            div.classList.add("review-card");
            div.innerHTML = `
                <h4>${review.title}</h4>
                <p>${review.content}</p>
                <small>Rating: ${review.rating} ⭐</small>
            `;
            container.appendChild(div);
        });
    } catch (error) {
        console.error("Error fetching reviews:", error);
    }
}

// ========== PAYMENTS SECTION (COMING SOON) ==========
function initiatePayment(amount) {
    console.log(`Initiating payment of $${amount}...`);
    alert("Payment feature coming soon!");
}

// ========== EVENT LISTENERS ==========
document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed.");
    fetchReviews();
});
