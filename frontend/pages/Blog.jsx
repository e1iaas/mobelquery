import { Link } from "react-router-dom"

const posts = [
  {
    slug: "/blog/scandinavian-furniture-trends-2026",
    category: "Trends · 2026",
    title: "Scandinavian Furniture Trends 2026: Earthy, Curved and Built to Last",
    excerpt: "Earthy tones, curved shapes, oak wood and sustainability — here's what's defining Nordic interiors this year.",
  },
  {
    slug: "/blog/how-to-find-scandinavian-furniture-online",
    category: "Guide · Shopping",
    title: "How to Find Scandinavian Furniture Online Without the Endless Scrolling",
    excerpt: "You know the feeling you want. Here's how to actually find it without wasting hours on filters that miss the point.",
  },
  {
    slug: "/blog/furnish-small-apartment-scandinavian-style",
    category: "Guide · Small Spaces",
    title: "How to Furnish a Small Apartment with Scandinavian Style",
    excerpt: "Small spaces and Scandinavian design are a natural match. Make the most of every square metre without sacrificing style.",
  },
]

export default function Blog() {
  return (
    <main className="flex-1 w-full">
      <div className="max-w-2xl mx-auto px-6 pt-16 pb-20">

        <div className="mb-12">
          <p className="text-xs text-orange-700 uppercase tracking-widest font-semibold mb-3">Blog</p>
          <h1 className="text-4xl font-bold text-gray-900 tracking-tight">
            Furniture guides &<br />
            <span className="text-orange-700">Comfort living</span>
          </h1>
        </div>

        <div className="flex flex-col gap-10">
          {posts.map((post) => (
            <Link key={post.slug} to={post.slug} className="group block border-b border-stone-100 pb-10">
              <p className="text-xs text-stone-400 uppercase tracking-widest mb-2">{post.category}</p>
              <h2 className="text-xl font-bold text-stone-800 group-hover:text-orange-700 transition-colors leading-snug mb-2">
                {post.title}
              </h2>
              <p className="text-stone-500 text-sm leading-relaxed">{post.excerpt}</p>
              <span className="inline-block mt-3 text-orange-700 text-sm font-semibold group-hover:underline">
                Read more →
              </span>
            </Link>
          ))}
        </div>

      </div>
    </main>
  )
}