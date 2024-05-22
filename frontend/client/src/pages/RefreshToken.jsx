// import React, { useEffect } from 'react';
// import axios from 'axios';

// const RefreshToken = () => {

//   useEffect(() => {
//     const refreshAccessToken = async () => {
//       try {
//         const token = localStorage.getItem("accessToken");
//         if (token) {
//           const config = {
//             headers: {
//               "Authorization":`Bearer ${token}`
//             }
//           }
//         console.log('Refreshing access token...');
//         const refreshToken = localStorage.getItem('refreshToken');
       
//         const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/', config,{
//           refresh: refreshToken

//         });
//       }
//         console.log(response)
//         const accessToken = response.data.tokens.access;
//         localStorage.setItem('accessToken', accessToken);
//         // Optionally, you can also update the expiration time of the access token if provided by the backend
//         const accessTokenExpiration = response.data.expires_in; // Adjust the key according to your backend response
//         if (accessTokenExpiration) {
//           const expirationTime = new Date(Date.now() + accessTokenExpiration * 1000);
//           localStorage.setItem('accessTokenExpiration', expirationTime);
//         }
//       } catch (error) {
//         console.error('Error refreshing token:', error);
//         // Handle token refresh failure
//       }
//     };

//     const checkAndRefreshToken = async () => {
//       const accessTokenExpiration = localStorage.getItem('accessTokenExpiration');
//       if (!accessTokenExpiration || new Date() >= new Date(accessTokenExpiration)) {
//         await refreshAccessToken();
//       }
//     };

//     checkAndRefreshToken();

//     // Optionally, you can set up a periodic check to refresh the token before it expires completely
//     const refreshTokenInterval = setInterval(() => {
//       checkAndRefreshToken();
//     }, 600000); // Refresh token every 10 minutes (adjust as needed)

//     return () => {
//       clearInterval(refreshTokenInterval); // Cleanup: clear the interval when the component unmounts
//     };
//   }, []);

//   return null; // This component doesn't render anything visible
// };

// export default RefreshToken;
