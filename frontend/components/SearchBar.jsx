export default function SearchBar({ value, onChange, onSubmit }) {
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit();
      }}
      className="w-full max-w-2xl mx-auto"
    >
      <div className="flex items-center bg-white border border-stone-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition-shadow">

        {/* Search icon */}
        <div className="pl-4 text-stone-400">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="11" cy="11" r="8" />
            <path d="M21 21l-4.35-4.35" />
          </svg>
        </div>

        {/* Input */}
        <input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Search..."
          className="flex-1 px-3 py-4 text-sm text-stone-800 placeholder-stone-400 focus:outline-none bg-transparent"
        />

        {/* Button */}
        <div className="pr-2">
          <button
            type="submit"
            className="bg-orange-700 text-white text-xs font-semibold px-5 py-2 rounded-xl hover:bg-orange-600 transition-colors"
          >
            Search →
          </button>
        </div>

      </div>
    </form>
  );
}