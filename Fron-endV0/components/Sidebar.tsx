'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Flame, TrendingUp } from 'lucide-react'

interface SidebarProps {
  showOnMobile?: boolean
}

export function Sidebar({ showOnMobile = false }: SidebarProps) {
  const trendingTopics = [
    { name: 'Remote Work', count: 245 },
    { name: 'Career Growth', count: 198 },
    { name: 'Company Culture', count: 167 },
    { name: 'Team Leadership', count: 145 },
    { name: 'Work-Life Balance', count: 132 },
  ]

  const upcomingEvents = [
    {
      id: '1',
      title: 'Tech Summit 2024',
      date: 'Apr 15, 2024',
      category: 'conference',
    },
    {
      id: '2',
      title: 'Leadership Workshop',
      date: 'Apr 18, 2024',
      category: 'workshop',
    },
    {
      id: '3',
      title: 'Career Growth Webinar',
      date: 'Apr 22, 2024',
      category: 'webinar',
    },
  ]

  return (
    <div className={`space-y-6 ${showOnMobile ? '' : 'hidden lg:block'}`}>
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
                <span className="text-xs text-muted-foreground">
                  {topic.count}
                </span>
              </div>
            </button>
          ))}
        </div>
      </Card>

      {/* Upcoming Events */}
      <Card className="p-6">
        <div className="flex items-center gap-2 mb-4">
          <Flame className="w-5 h-5 text-accent" />
          <h3 className="font-semibold text-foreground">Upcoming Events</h3>
        </div>
        <div className="space-y-4">
          {upcomingEvents.map((event) => (
            <button
              key={event.id}
              className="w-full text-left hover:bg-muted p-3 rounded-lg transition-colors border border-border"
            >
              <div className="mb-2">
                <Badge variant="secondary" className="text-xs">
                  {event.category}
                </Badge>
              </div>
              <h4 className="text-sm font-medium text-foreground mb-1 line-clamp-2">
                {event.title}
              </h4>
              <p className="text-xs text-muted-foreground">{event.date}</p>
            </button>
          ))}
        </div>
      </Card>
    </div>
  )
}
