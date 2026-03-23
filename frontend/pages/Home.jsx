// Home.jsx
import SearchBar from "../components/SearchBar"
import ProductCard from "../components/ProductCard"
import SkeletonCard from "../components/SkeletonCard"
import HowItWorks from "../components/HowItWorks"
import { useState, useEffect } from "react"

const exampleTags = [
  "Cozy sofa for small living room",
  "Minimalist oak dining table",
]


export default function Home() {
  const [loading, setLoading] = useState(false)
  const [query, setQuery] = useState("")
  const [data, setData] = useState([])
  const [page, setPage] = useState({ page_number: 1})
  const [submittedQuery, setSumbittedQuery] = useState("")

  const fetchProducts = (q, pageNum) => {
    if (loading) return

    setLoading(true)
    fetch(`https://api.mobelquery.com/api/?q=${encodeURIComponent(q)}&page=${pageNum}`)
      .then(res => res.json())
      .then(json => {
        console.log(json)
        setData(json.results ?? [])
        setPage(json.page_obj ?? [])
      })
      .catch(err => console.error(err))
      .finally(() => setLoading(false))
  }

  //add guard for search so skeletoncards doesnt always load on page boot
  
  useEffect(() => {
    if(!submittedQuery) return
    fetchProducts(submittedQuery,page.page_number)
  },[page.page_number])

  const handleSearch = () => {
    setSumbittedQuery(query)
    setPage({page_number: 1})
    fetchProducts(query,1)
  }


return (
  <main className="flex-1 w-full">
    {/* Hero headline - only show when no results yet */}
    {data.length === 0 && !loading && (
      <div className="max-w-2xl mx-auto px-6 pt-16 pb-6 text-center">
        <h1 className="text-4xl font-bold text-gray-900 tracking-tight">
          Search furniture the way<br />
          <span className="text-orange-700">you think about it</span>
        </h1>
        <p className="mt-3 text-gray-500 text-base">
          Describe what you're looking for — we'll find it across verified EU stores.
        </p>
      </div>
    )}

    {/* Search bar */}
    <div className="max-w-6xl mx-auto px-6 pt-8 pb-4">
      <SearchBar value={query} onChange={setQuery} onSubmit={handleSearch} />
    </div>

    {data.length === 0 && !loading && (
  <div className="max-w-2xl mx-auto px-6 pb-6 flex flex-wrap gap-2 justify-center">
    {exampleTags.map((tag) => (
      <button
        key={tag}
        onClick={() => {
          setQuery(tag)
          setSumbittedQuery(tag)
          fetchProducts(tag, 1)
        }}
        className="text-sm text-gray-600 bg-gray-100 hover:bg-orange-50 hover:text-orange-700 border border-gray-200 hover:border-orange-300 px-3 py-1.5 rounded-full transition-colors"
      >
        {tag}
      </button>
    ))}
  </div>
)}

{/* How it works */}
{data.length == 0 && !loading && (<HowItWorks /> )}

    {/* Grid feed */}
    <div className="max-w-6xl mx-auto px-6 pb-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {loading ? Array(12).fill(0).map((_,i) => <SkeletonCard key={i}/>):
        data.map(d => (
          <ProductCard
            key={d.id}
            title={d.name}
            url={d.url}
            image={d.image}
            available={d.available}
            price={d.price}
            currency={d.currency}
            description={d.description}
            brand={d.brand}
          />
        ))}
      </div>
      <div className="flex justify-center mt-6 space-x-32">
        {page.has_prev ? (
          <button onClick={() => setPage(prev => ({ ...prev, page_number: prev.page_number + 1 }))}
          className="bg-orange-700 text-white text-xs font-semibold px-5 py-2 rounded-xl hover:bg-orange-600 transition-colors">
           ← Previous</button>
        ) : null}

        
       {page.has_next ? (
          <button onClick={() => setPage(prev => ({ ...prev, page_number: prev.page_number + 1 }))}
          className="bg-orange-700 text-white text-xs font-semibold px-5 py-2 rounded-xl hover:bg-orange-600 transition-colors">
           Next →</button>
        ) : null}
        </div>
    </div>
  </main>
)
}