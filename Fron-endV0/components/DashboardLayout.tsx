'use client'

import Link from 'next/link'
import { Button } from '@/components/ui/button'
import {
  BarChart3,
  TrendingUp,
  Zap,
  FileText,
  Menu,
  X,
} from 'lucide-react'
import { useState } from 'react'

interface DashboardLayoutProps {
  children: React.ReactNode
  currentSection?: string
}

export function DashboardLayout({
  children,
  currentSection = 'overview',
}: DashboardLayoutProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const navItems = [
    {
      label: 'Overview',
      href: '/dashboard',
      icon: BarChart3,
      section: 'overview',
    },
    {
      label: 'Insights',
      href: '/dashboard/insights',
      icon: TrendingUp,
      section: 'insights',
    },
    {
      label: 'Event Impact',
      href: '/dashboard/event-impact',
      icon: Zap,
      section: 'event-impact',
    },
    {
      label: 'Experiences',
      href: '/dashboard/experiences',
      icon: FileText,
      section: 'experiences',
    },
  ]

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Mobile menu button */}
      <div className="md:hidden fixed top-16 right-4 z-40">
        <Button
          variant="ghost"
          size="icon"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          {mobileMenuOpen ? (
            <X className="w-5 h-5" />
          ) : (
            <Menu className="w-5 h-5" />
          )}
        </Button>
      </div>

      {/* Sidebar */}
      <aside
        className={`${
          mobileMenuOpen ? 'block' : 'hidden md:block'
        } w-full md:w-64 border-r border-border bg-muted/30 pt-20 md:pt-6`}
      >
        <nav className="px-4 space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon
            const isActive = currentSection === item.section

            return (
              <Link key={item.href} href={item.href}>
                <button
                  onClick={() => setMobileMenuOpen(false)}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-primary/10 text-primary'
                      : 'text-muted-foreground hover:bg-muted hover:text-foreground'
                  }`}
                >
                  <Icon className="w-4 h-4 flex-shrink-0" />
                  <span>{item.label}</span>
                </button>
              </Link>
            )
          })}
        </nav>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto">
        <div className="h-full md:max-h-screen md:overflow-y-auto">
          {children}
        </div>
      </main>
    </div>
  )
}
