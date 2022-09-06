import './App.css';
import Navbar from './components/navbar/navbar'
import HomePage from './components/homepage/homepage'
import Footer from './components/footer/footer'
import SearchPage from './components/search-page/search-page'
import PrivacyPolicy from './components/privacy-policy/privacy-policy'
import { 
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom'
function App() {
  console.log("Welcome To Lexata...")
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={ <SearchPage /> } />
          <Route path="/privacy" element={ <PrivacyPolicy /> } />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
