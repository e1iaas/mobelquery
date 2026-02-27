import Home from "../pages/Home.jsx"
import Privacy from "../pages/Privacy.jsx"
import Terms from "../pages/Terms.jsx"
import Header from "../components/Header.jsx"
import Footer from "../components/Footer.jsx"
import {Routes, Route} from "react-router-dom"

function App() {
  

return (
  <div className="min-h-screen flex flex-col">
    <Header />
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/privacy" element={<Privacy />}/>
        <Route path="/terms" element={<Terms />}/>
      </Routes>
    <Footer />
  </div>
)
}

export default App