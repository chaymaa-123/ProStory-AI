'use client'

import { useTheme } from 'next-themes'
import { Menu, Moon, Sun, X } from 'lucide-react'
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

  useEffect(() => {
    setMounted(true)
  }, [])

  const navItems = [
    { label: 'Feed', href: '/feed' },
    { label: 'Events', href: '/events' },
    { label: 'Dashboard', href: '/dashboard' },
  ]

  const isActive = (href: string) => currentPath === href

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="w-full max-w-7xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 font-semibold text-lg">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-accent flex items-center justify-center text-white font-bold">
              C
            </div>
            <span className="hidden sm:inline text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent font-bold">Connex</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`text-sm font-medium transition-colors ${
                  isActive(item.href)
                    ? 'text-primary'
                    : 'text-muted-foreground hover:text-foreground'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>

          {/* Right side actions */}
          <div className="flex items-center gap-2">
            {mounted && (
              <Button
                variant="ghost"
                size="icon"
                onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
                className="rounded-lg"
              >
                {theme === 'dark' ? (
                  <Sun className="w-5 h-5" />
                ) : (
                  <Moon className="w-5 h-5" />
                )}
              </Button>
            )}

            <Link href="/auth">
              <Button
                variant="default"
                size="sm"
                className="hidden sm:inline-flex rounded-lg"
              >
                Se connecter
              </Button>
            </Link>

            {/* Mobile menu button */}
            <Button
              variant="ghost"
              size="icon"
              className="md:hidden"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? (
                <X className="w-5 h-5" />
              ) : (
                <Menu className="w-5 h-5" />
              )}
            </Button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="md:hidden border-t border-border py-4 space-y-2">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`block px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  isActive(item.href)
                    ? 'bg-primary/10 text-primary'
                    : 'text-muted-foreground hover:bg-muted hover:text-foreground'
                }`}
                onClick={() => setMobileMenuOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="px-4 pt-2 border-t border-border">
              <Link href="/auth" className="block w-full">
                <Button
                  variant="default"
                  size="sm"
                  className="w-full rounded-lg"
                >
                  Se connecter
                </Button>
              </Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}
