// ProductCard.jsx
export default function ProductCard({ title, image, url, available, price, currency, description, brand }) {
  return (
    <div className="bg-white border border-gray-200 rounded-2xl shadow-sm flex flex-col overflow-hidden hover:shadow-md transition-shadow">

      {/* Image */}
      <a href={url} className="block overflow-hidden bg-stone-50">
        <img
          src={image}
          alt={title}
          className="w-full h-52 object-contain hover:scale-105 transition-transform duration-300"
        />
      </a>

      {/* Content */}
      <div className="p-4 flex flex-col flex-grow">

        {/* Availability pill + Brand tag */}
        <div className="mb-2 flex items-center gap-2 flex-wrap">
          <span className={`text-xs font-medium px-2 py-1 rounded-full ${available ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-500'}`}>
            {available ? '● In stock' : '● Out of stock'}
          </span>
          {brand && (
            <span className="text-xs font-semibold px-2 py-1 rounded-full bg-stone-100 text-stone-500 uppercase tracking-wide">
              {brand}
            </span>
          )}
        </div>

        {/* Title */}
        <a href={url}>
          <h3 className="text-sm font-medium text-gray-800 hover:text-green-800 line-clamp-3 mb-2 leading-snug">
            {title}
          </h3>
        </a>

        {/* Description */}
        {description && (
          <p className="text-xs text-gray-400 line-clamp-2 mb-3 leading-relaxed">
            {description}
          </p>
        )}

        {/* Price + Button */}
        <div className="mt-auto flex items-center justify-between gap-3">
          <span className="text-lg font-bold text-gray-900">{price} {currency}</span>
          <a
            href={url}
            className="bg-orange-700 text-white text-xs font-semibold px-4 py-2 rounded-xl hover:bg-orange-600 transition-colors whitespace-nowrap"
          >
            View product →
          </a>
        </div>

      </div>
    </div>
  )
}