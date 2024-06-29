// Fetch user data and populate the webpage
const keys = ['season', 'username', 'matching_colors', 'best_hair_color']; // Specify the keys you want to retrieve
const queryParams = keys.map(key => `keys=${encodeURIComponent(key)}`).join('&');

fetch('/user/data?' + queryParams, {
    method: 'GET',
})
.then(response => {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error('Failed to fetch user data');
    }
})
.then(userData => {
    console.log(userData)

    document.getElementById('userName').textContent = userData.username;
    document.getElementById('userSeason').textContent = userData.season;
    
    const matchingColorsSpan = document.getElementById('userColors');
    for (const colorName in userData.matching_colors) {
        const colorHex = userData.matching_colors[colorName];
        const colorDiv = document.createElement('div');
        colorDiv.textContent = `${colorName}: ${colorHex}`;
        colorDiv.style.backgroundColor = colorHex;
        matchingColorsSpan.appendChild(colorDiv);
    }
    
    const hairColorsSpan = document.getElementById('userHairColors');
    for (const colorName in userData.best_hair_color) {
        const colorHex = userData.best_hair_color[colorName];
        const colorDiv = document.createElement('div');
        colorDiv.textContent = `${colorName}: ${colorHex}`;
        colorDiv.style.backgroundColor = colorHex;
        hairColorsSpan.appendChild(colorDiv);
    }
})
.catch(error => {
    console.error('Error fetching user data:', error);
});


document.addEventListener('DOMContentLoaded', function() {
    // Event listener for sign-out button
    document.getElementById('signOutBtn').addEventListener('click', function() {
        // Assuming you have a sign-out endpoint '/signout'
        fetch('http://127.0.0.1:5001/user/signout', {
            method: 'GET',
        })
        .then(response => {
            if (response.ok) {
                // Sign out successful, redirect to login page or perform any other action
                window.location.href = '/index/'; // Redirect to login page
            } else {
                // Handle sign out failure
                console.error('Sign out failed:', response.statusText);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
  });
  
  document.getElementById('uploadBtn').addEventListener('click', function() {
    window.location.href = '/upload/';
  });
