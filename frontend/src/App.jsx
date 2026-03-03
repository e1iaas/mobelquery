import Home from "../pages/Home.jsx"
import Privacy from "../pages/Privacy.jsx"
import Terms from "../pages/Terms.jsx"
import About from "../pages/About.jsx"
import Blog from "../pages/Blog.jsx"
import BlogPost from "../pages/BlogPost.jsx"
import Header from "../components/Header.jsx"
import Footer from "../components/Footer.jsx"
import CookieBanner from "../components/CookieBanner.jsx"
import {Routes, Route} from "react-router-dom"

function App() {
  

return (
  <div className="min-h-screen flex flex-col">
    <Header />
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/privacy" element={<Privacy />}/>
        <Route path="/terms" element={<Terms />}/>
        <Route path="/about" element={<About />}/>
        <Route path="/blog" element={<Blog />}/>
        <Route path="/blog/:slug" element={<BlogPost />} />
      </Routes>
    <Footer />
    <CookieBanner />
  </div>
)
}

export default App