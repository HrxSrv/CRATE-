// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth}  from "firebase/auth"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCekQbvWS3sm8KUSe9izrdY02CZkGQLPKM",
  authDomain: "crate-491ad.firebaseapp.com",
  databaseURL: "https://crate-491ad-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "crate-491ad",
  storageBucket: "crate-491ad.appspot.com",
  messagingSenderId: "52910803364",
  appId: "1:52910803364:web:0ac9cb3204dc1818509931",
  measurementId: "G-X5R1ZJ74FN"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app)
export const analytics = getAnalytics(app);