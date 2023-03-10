import {useEffect, useState} from "react";

const API_URL = "https://www.goodreads.com/search.xml?key=YOUR_KEY&q=Ender%27s+Game"

const App = () => {

    const searchBook = async(title) => {
        const response = await fetch(`${API_URL}&s=${title}`);
        const data = await response.json();

        console.log(data.Search);
    }

    useEffect(() => {
        searchBook('Animal Farm')
    }, []);

    return (
        <div className="app">
            <h1>TheBookMark</h1>

            <div className="search">
                <input
                    placeholder="Search for books, authors" 
                    value=""
                    onChange={()=>{}}></input>
            </div>

            <div className="container">
                
            </div>
        </div>

       
    );
}

export default App;




// import { useState } from 'react'
// import axios from "axios";
// import logo from './logo.svg';
// import './App.css';

// function App() {

//   const [profileData, setProfileData] = useState(null)

//   function getData() {
//     axios({
//       method: "GET",
//       url:"/profile",
//     })
//     .then((response) => {
//       const res =response.data
//       setProfileData(({
//         profile_name: res.Name,
//         about_me: res.AboutMe}))
//     }).catch((error) => {
//       if (error.response) {
//         console.log(error.response)
//         console.log(error.response.status)
//         console.log(error.response.headers)
//         }
//     })}

//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>

//         {/* new line start*/}
//         <p>To get your profile details: </p><button onClick={getData}>Click me</button>
//         {profileData && <div>
//               <p>Profile name: {profileData.profile_name}</p>
//               <p>About me: {profileData.about_me}</p>
//             </div>
//         }
//          {/* end of new line */}
//       </header>
//     </div>
//   );
// }

// export default App;