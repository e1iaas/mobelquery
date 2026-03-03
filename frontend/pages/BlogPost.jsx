import { useParams, Link } from "react-router-dom";
import { blogPosts } from "./content/BlogPost";

export default function BlogPost() {
  let params = useParams()
  let post = blogPosts.find(p => p.slug == params.slug)

  if (!post) return <p>Loading...</p>

  return (
    <main className="flex-1 w-full">
      <div className="max-w-2xl mx-auto px-6 pt-16 pb-20">

        <Link to="/blog" className="text-xs text-orange-700 uppercase tracking-widest font-semibold hover:underline">
          ← Blog
        </Link>

        <div className="mt-6 mb-10">
          <p className="text-xs text-stone-400 uppercase tracking-widest mb-3">{post.category}</p>
          <h1 className="text-4xl font-bold text-gray-900 tracking-tight leading-tight">
            {post.title}
          </h1>
          <p className="mt-4 text-stone-500 text-base leading-relaxed">{post.excerpt}</p>
        </div>

        <div className="flex flex-col gap-8">
          {post.sections.map((section) => (
            <div key={section.heading}>
              <h2 className="text-xl font-bold text-stone-800 mb-3">{section.heading}</h2>
              <p className="text-stone-600 leading-relaxed">{section.text}</p>
            </div>
          ))}
        </div>

        <div className="mt-12 border-t border-stone-200 pt-10 text-center">
          <p className="text-stone-500 mb-4 text-sm">Looking for Scandinavian furniture?</p>
          <Link
            to="/"
            className="inline-block bg-orange-700 text-white text-sm font-semibold px-6 py-3 rounded-xl hover:bg-orange-600 transition-colors"
          >
            Search on MobelQuery →
          </Link>
        </div>

      </div>
    </main>
  )
}