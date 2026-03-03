import { useState, useEffect } from "react";

export default function CookieBAnner(){
    const [visible, setVisible] = useState(false)

    useEffect(() => {
        const consent = localStorage.getItem("cookie_consent")
        if(!consent)setVisible(true)
    }, [])

    const accept = () => {
        localStorage.setItem("cookie_consent", "accepted")
        setVisible(false)
        loadCookie("https://www.googletagmanager.com/gtag/js?id=G-J8BGWR3C4S")
    }

    const decline = () => {
        localStorage.setItem("cookie_consent", "declined")
        setVisible(false)
    }

    const loadCookie = (url) => {
        //create append load
        let cookieScript = document.createElement('script')
        let cookieSrc = document.createElement('script')

         cookieScript.addEventListener('load', () => {
            console.log("cookie loaded")
            cookieScript.script = window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-J8BGWR3C4S');
        })

        cookieScript.addEventListener('error', () => {
            console.error("Error loading cookie")
        })

        cookieSrc.addEventListener('load', () => {
            console.log("cookie loaded")

        })

        cookieSrc.addEventListener('error', () => {
            console.error("Error loading cookie src")
        })

        cookieSrc.src = url
        document.head.appendChild(cookieSrc)
        document.head.appendChild(cookieScript)


    }

    if(!visible) return null


    return (
    <div className="fixed bottom-0 left-0 right-0 z-50 bg-stone-900 border-t border-stone-700 px-6 py-4">
      <div className="max-w-5xl mx-auto flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <p className="text-stone-300 text-sm leading-relaxed">
          We use cookies to improve your experience and analyse site traffic. By continuing, you agree to our{" "}
          <a href="/privacy" className="text-orange-400 hover:underline">Privacy Policy</a>.
        </p>
        <div className="flex gap-3 flex-shrink-0">
          <button
            onClick={decline}
            className="text-stone-400 text-sm font-medium hover:text-stone-200 transition-colors px-3 py-1.5"
          >
            Decline
          </button>
          <button
            onClick={accept}
            className="bg-orange-700 text-white text-sm font-semibold px-5 py-1.5 rounded-lg hover:bg-orange-600 transition-colors"
          >
            Accept
          </button>
        </div>
      </div>
    </div>
  )
}