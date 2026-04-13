'use client'

import { useTheme } from 'next-themes'
import { Menu, Moon, Sun, X, LogOut } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { useState, useEffect } from 'react'
import Link from 'next/link'

interface NavigationProps {
  currentPath?: string
}

export function Navigation({ currentPath = '/' }: NavigationProps) {
  const { theme, setTheme } = useTheme()
  const [mounted, setMounted] = useState(false)
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [user, setUser] = useState<{ role: string; name: string } | null>(null)

  // 1. Initialisation au montage du composant
  useEffect(() => {
    setMounted(true)
    const savedUser = localStorage.getItem('user')
    if (savedUser) {
      try {
        const parsed = JSON.parse(savedUser)
        if (parsed && typeof parsed === 'object') setUser(parsed)
      } catch (e) {
        console.error("Erreur session", e)
      }
    }
  }, [])

  // 2. Définition des liens selon l'utilisateur
  // On ne calcule les liens que si l'utilisateur est présent
  const navItems = user ? (
    user.role === 'entreprise' 
      ? [{ label: '', href: '/dashboard' }]
      : [
          { label: 'Feed', href: '/feed' },
          { label: 'Expériences', href: '/events' },
          { label: 'Profil', href: '/profile' } // À adapter vers ta page d'expériences
        ]
  ) : []

  const isActive = (href: string) => currentPath === href

  const handleLogout = () => {
    localStorage.removeItem('user')
    localStorage.removeItem('token')
    window.location.href = '/'
  }

  // Éviter l'erreur d'hydratation (mismatch serveur/client)
  if (!mounted) {
    return (
      <nav className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur h-16">
        <div className="w-full max-w-7xl mx-auto px-4 h-full flex items-center justify-between">
          <div className="font-semibold text-lg flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-primary/20" />
            <span className="text-primary/20">Connex</span>
          </div>
        </div>
      </nav>
    )
  }

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="w-full max-w-7xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          
          {/* LOGO */}
          <Link href="" className="flex items-center gap-2 font-semibold text-lg hover:opacity-90 transition-opacity">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-accent flex items-center justify-center text-white font-bold">
              C
            </div>
            <span className="hidden sm:inline text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent font-bold">Connex</span>
          </Link>

          {/* DESKTOP NAV (Visible seulement si connecté) */}
          <div className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`text-sm font-medium transition-colors ${
                  isActive(item.href) ? 'text-primary' : 'text-muted-foreground hover:text-foreground'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>

          {/* ACTIONS */}
          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
              className="rounded-lg"
            >
              {theme === 'dark' ? <Sun className="w-5 h-5 text-yellow-500" /> : <Moon className="w-5 h-5" />}
            </Button>

            {user ? (
              <Button
                variant="default"
                size="sm"
                className="hidden sm:inline-flex rounded-lg px-6 font-bold"
                onClick={handleLogout}
              >
                <LogOut className="w-4 h-4 mr-2" />
                Quitter 
              </Button>
            ) : (
              <Link href="/auth/login">
                <Button variant="default" size="sm" className="hidden sm:inline-flex rounded-lg px-6 font-bold">
                  Se connecter
                </Button>
              </Link>
            )}

            {/* MOBILE MENU BUTTON */}
            {navItems.length > 0 && (
              <Button
                variant="ghost" size="icon" className="md:hidden"
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              >
                {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
              </Button>
            )}
          </div>
        </div>

        {/* MOBILE NAV MENU */}
        {mobileMenuOpen && navItems.length > 0 && (
          <div className="md:hidden border-t border-border py-4 space-y-2 animate-in slide-in-from-top-2">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`block px-4 py-3 rounded-lg text-sm font-bold transition-colors ${
                  isActive(item.href) ? 'bg-primary/10 text-primary' : 'text-muted-foreground hover:bg-muted'
                }`}
                onClick={() => setMobileMenuOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="px-4 pt-2 border-t border-border mt-2">
              <Button 
                variant="ghost" 
                className="sm:inline-flex rounded-lg px-6 font-bold"
                onClick={handleLogout}
              >
                <LogOut className="w-4 h-4 mr-3" />
                Déconnexion
              </Button>
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}
