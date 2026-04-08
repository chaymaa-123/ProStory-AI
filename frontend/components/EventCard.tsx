'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Calendar, MapPin, Users } from 'lucide-react'

interface EventCardProps {
  id: string
  title: string
  date: string
  time?: string
  location?: string
  category: string
  description: string
  attendees: number
  relatedExperiences: number
  image?: string
  onClick?: () => void
}

export function EventCard({
  id,
  title,
  date,
  time,
  location,
  category,
  description,
  attendees,
  relatedExperiences,
  image,
  onClick,
}: EventCardProps) {
  const categoryColors: Record<string, string> = {
    conference: 'bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300',
    workshop: 'bg-purple-100 text-purple-800 dark:bg-purple-900/40 dark:text-purple-300',
    webinar: 'bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-300',
    meetup: 'bg-orange-100 text-orange-800 dark:bg-orange-900/40 dark:text-orange-300',
  }

  return (
    <Card
      className="overflow-hidden hover:shadow-md transition-all duration-200 cursor-pointer h-full flex flex-col"
      onClick={onClick}
    >
      {/* Event image placeholder */}
      {image && (
        <div className="w-full h-40 bg-gradient-to-br from-primary/20 to-accent/20 overflow-hidden">
          <img
            src={image}
            alt={title}
            className="w-full h-full object-cover"
          />
        </div>
      )}

      <div className="p-6 flex-1 flex flex-col">
        {/* Category badge */}
        <div className="mb-3">
          <Badge
            variant="outline"
            className={categoryColors[category] || categoryColors.conference}
          >
            {category}
          </Badge>
        </div>

        {/* Title */}
        <h3 className="font-semibold text-lg text-balance text-foreground mb-2 line-clamp-2">
          {title}
        </h3>

        {/* Description */}
        <p className="text-sm text-muted-foreground mb-4 line-clamp-2 flex-1">
          {description}
        </p>

        {/* Details */}
        <div className="space-y-3 py-3 border-t border-border">
          <div className="flex items-center gap-2 text-sm text-foreground">
            <Calendar className="w-4 h-4 text-accent flex-shrink-0" />
            <span>
              {date}
              {time && ` at ${time}`}
            </span>
          </div>

          {location && (
            <div className="flex items-center gap-2 text-sm text-foreground">
              <MapPin className="w-4 h-4 text-accent flex-shrink-0" />
              <span className="truncate">{location}</span>
            </div>
          )}

          <div className="flex items-center justify-between text-xs text-muted-foreground">
            <div className="flex items-center gap-1">
              <Users className="w-4 h-4" />
              <span>{attendees} attending</span>
            </div>
            <span>{relatedExperiences} experiences</span>
          </div>
        </div>
      </div>
    </Card>
  )
}
