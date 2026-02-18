import Home from "../pages/Home"
import Privacy from "../pages/Privacy"
import Terms from "../pages/Terms"
import Header from "../components/Header"
import Footer from "../components/Footer"
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