'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Flame, TrendingUp, Calendar, MapPin, Loader2 } from 'lucide-react'
import { useState, useEffect } from 'react'
import Link from 'next/link'

interface SidebarProps {
  showOnMobile?: boolean
}

interface UpcomingEvent {
  id: string
  title: string
  date: string
  location: string
  category: string
  company_name?: string
  is_virtual?: boolean
}

const CATEGORY_COLORS: Record<string, string> = {
  Technologie:   'bg-blue-500/10 text-blue-400 border-blue-500/20',
  Environnement: 'bg-green-500/10 text-green-400 border-green-500/20',
  Santé:         'bg-rose-500/10 text-rose-400 border-rose-500/20',
  Management:    'bg-purple-500/10 text-purple-400 border-purple-500/20',
  Carrière:      'bg-amber-500/10 text-amber-400 border-amber-500/20',
}

function formatEventDate(isoDate: string): string {
  const d = new Date(isoDate)
  return d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric' })
}

export function Sidebar({ showOnMobile = false }: SidebarProps) {
  const [upcomingEvents, setUpcomingEvents] = useState<UpcomingEvent[]>([])
  const [isLoading, setIsLoading] = useState(true)

  const trendingTopics = [
    { name: 'Remote Work',       count: 245 },
    { name: 'Career Growth',     count: 198 },
    { name: 'Company Culture',   count: 167 },
    { name: 'Team Leadership',   count: 145 },
    { name: 'Work-Life Balance', count: 132 },
  ]

  useEffect(() => {
    const fetchUpcomingEvents = async () => {
      try {
        const res = await fetch(
          `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'}/events/upcoming?limit=4`
        )
        if (!res.ok) throw new Error('API error')
        const data: UpcomingEvent[] = await res.json()
        setUpcomingEvents(data)
      } catch {
        // Fallback: événements maquettes à venir (TechNova & EcoFuture)
        setUpcomingEvents([
          {
            id:           'mock-1',
            title:        'Tech Summit 2026 – Casablanca',
            date:         '2026-05-28T09:00:00Z',
            location:     'Casablanca, Maroc',
            category:     'Technologie',
            company_name: 'TechNova Solutions',
            is_virtual:   false,
          },
          {
            id:           'mock-2',
            title:        'Webinar – Bâtiments à énergie positive',
            date:         '2026-05-22T14:00:00Z',
            location:     'En ligne',
            category:     'Environnement',
            company_name: 'EcoFuture Group',
            is_virtual:   true,
          },
          {
            id:           'mock-3',
            title:        'Sustainability Week 2026',
            date:         '2026-06-10T09:00:00Z',
            location:     'Rabat, Maroc',
            category:     'Environnement',
            company_name: 'EcoFuture Group',
            is_virtual:   false,
          },
          {
            id:           'mock-4',
            title:        'AI & Data Day – Rabat',
            date:         '2026-06-18T10:00:00Z',
            location:     'Rabat, Maroc',
            category:     'Technologie',
            company_name: 'TechNova Solutions',
            is_virtual:   false,
          },
        ])
      } finally {
        setIsLoading(false)
      }
    }
    fetchUpcomingEvents()
  }, [])

  return (
    <div className={`space-y-6 p-4 ${showOnMobile ? '' : 'hidden lg:block'}`}>
      {/* Trending Topics */}
      <Card className="p-6">
        <div className="flex items-center gap-2 mb-4">
          <TrendingUp className="w-5 h-5 text-accent" />
          <h3 className="font-semibold text-foreground">Trending Topics</h3>
        </div>
        <div className="space-y-3">
          {trendingTopics.map((topic) => (
            <button
              key={topic.name}
              className="w-full text-left hover:bg-muted p-2 rounded-lg transition-colors"
            >
              <div className="flex items-center justify-between">
                <span className="text-sm font-medium text-foreground hover:text-primary">
                  {topic.name}
                </span>
                <span className="text-xs text-muted-foreground">{topic.count}</span>
              </div>
            </button>
          ))}
        </div>
      </Card>

      {/* Upcoming Events */}
      <Card className="p-6">
        <div className="flex items-center gap-2 mb-4">
          <Flame className="w-5 h-5 text-accent" />
          <h3 className="font-semibold text-foreground">Événements à venir</h3>
        </div>

        {isLoading ? (
          <div className="flex justify-center py-6">
            <Loader2 className="w-5 h-5 animate-spin text-muted-foreground" />
          </div>
        ) : upcomingEvents.length === 0 ? (
          <p className="text-xs text-muted-foreground text-center py-4">
            Aucun événement à venir.
          </p>
        ) : (
          <div className="space-y-3">
            {upcomingEvents.map((event) => {
              const badgeClass =
                CATEGORY_COLORS[event.category] ??
                'bg-muted text-muted-foreground border-border'

              return (
                <Link
                  key={event.id}
                  href={`/events/${event.id}`}
                  className="block hover:bg-muted p-3 rounded-lg transition-colors border border-border group"
                >
                  {/* Category badge */}
                  <span
                    className={`inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium border mb-2 ${badgeClass}`}
                  >
                    {event.category}
                  </span>

                  {/* Title */}
                  <h4 className="text-sm font-medium text-foreground mb-1 line-clamp-2 group-hover:text-primary transition-colors">
                    {event.title}
                  </h4>

                  {/* Company name */}
                  {event.company_name && (
                    <p className="text-[11px] text-accent font-medium mb-1">
                      {event.company_name}
                    </p>
                  )}

                  {/* Date + location */}
                  <div className="flex items-center gap-1 text-[11px] text-muted-foreground">
                    <Calendar className="w-3 h-3 shrink-0" />
                    <span>{formatEventDate(event.date)}</span>
                    {!event.is_virtual && event.location && (
                      <>
                        <span className="mx-1">·</span>
                        <MapPin className="w-3 h-3 shrink-0" />
                        <span className="truncate">{event.location}</span>
                      </>
                    )}
                    {event.is_virtual && (
                      <>
                        <span className="mx-1">·</span>
                        <span className="text-blue-400">En ligne</span>
                      </>
                    )}
                  </div>
                </Link>
              )
            })}
          </div>
        )}

        <Link
          href="/events"
          className="block text-center text-xs text-accent hover:underline mt-4 font-medium"
        >
          Voir tous les événements →
        </Link>
      </Card>
    </div>
  )
}
