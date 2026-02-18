// Home.jsx
import SearchBar from "../components/SearchBar"
import ProductCard from "../components/ProductCard"
import { useState } from "react"

export default function Home() {
  const [loading, setLoading] = useState(false)
  const [query, setQuery] = useState("")
  const [data, setData] = useState([])

  const handleSearch = () => {
    if (loading) return

    setLoading(true)
    fetch(`http://127.0.0.1:8001/api/?q=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(json => setData(json.results))
      .catch(err => console.error(err))
      .finally(() => setLoading(false))
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
        {data.map(d => (
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
    </div>
  </main>
)
}