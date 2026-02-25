// Home.jsx
import SearchBar from "../components/SearchBar"
import ProductCard from "../components/ProductCard"
import SkeletonCard from "../components/SkeletonCard"
import { useState, useEffect } from "react"



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

  useEffect(() => {
    fetchProducts(submittedQuery,page.page_number)
  },[page.page_number])

  const handleSearch = () => {
    setSumbittedQuery(query)
    setPage({page_number: 1})
    fetchProducts(query,1)
  }


return (
  <main className="flex-1 w-full">
    {/* Search bar */}
    <div className="max-w-6xl mx-auto px-6 pt-8 pb-4">
      <SearchBar value={query} onChange={setQuery} onSubmit={handleSearch} />
    </div>

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