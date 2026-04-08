'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Heart, MessageCircle } from 'lucide-react'
import { useState } from 'react'

interface ExperienceCardProps {
  id: string
  title: string
  preview: string
  author: {
    name: string
    avatar?: string
  }
  tags: string[]
  event?: string
  likes: number
  comments: number
  sentiment?: 'positive' | 'neutral' | 'negative'
  date: string
}

export function ExperienceCard({
  id,
  title,
  preview,
  author,
  tags,
  event,
  likes,
  comments,
  date,
}: ExperienceCardProps) {
  const [isLiked, setIsLiked] = useState(false)

  const handleLike = (e: React.MouseEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setIsLiked(!isLiked)
  }

  return (
    <Card className="p-6 border border-border hover:shadow-md hover:border-primary/30 transition-all duration-200 cursor-pointer group">
      <div className="space-y-4">
        {/* Header */}
        <div className="flex items-start justify-between gap-4">
          <h3 className="font-semibold text-base leading-snug text-foreground group-hover:text-primary transition-colors line-clamp-3">
            {title}
          </h3>
        </div>

        {/* Preview text */}
        <p className="text-sm text-muted-foreground line-clamp-2">
          {preview}
        </p>

        {/* Tags */}
        {tags && tags.length > 0 && (
          <div className="flex gap-2 flex-wrap">
            {tags.slice(0, 3).map((tag) => (
              <Badge key={tag} variant="secondary" className="text-xs cursor-pointer hover:bg-secondary/80">
                {tag}
              </Badge>
            ))}
            {tags.length > 3 && (
              <Badge variant="secondary" className="text-xs">
                +{tags.length - 3}
              </Badge>
            )}
          </div>
        )}

        {/* Event badge if present */}
        {event && (
          <div className="inline-flex items-center gap-2 text-xs text-primary font-medium bg-primary/10 px-3 py-1 rounded-full">
            <span className="w-1.5 h-1.5 rounded-full bg-primary" />
            {event}
          </div>
        )}

        {/* Author and metadata */}
        <div className="flex items-center justify-between pt-3 border-t border-border/40">
          <div className="flex items-center gap-3 min-w-0">
            <div className="w-8 h-8 rounded-full bg-primary/10 flex-shrink-0 flex items-center justify-center">
              <span className="text-xs font-semibold text-primary">
                {author.name[0]?.toUpperCase()}
              </span>
            </div>
            <div className="min-w-0">
              <p className="text-xs font-medium text-foreground truncate">
                {author.name}
              </p>
              <p className="text-xs text-muted-foreground">
                {date}
              </p>
            </div>
          </div>

          {/* Actions */}
          <div className="flex items-center gap-4 ml-2 flex-shrink-0">
            <button
              onClick={handleLike}
              className="flex items-center gap-1 text-xs text-muted-foreground hover:text-red-500 transition-colors"
            >
              <Heart
                className={`w-4 h-4 transition-all ${
                  isLiked ? 'fill-red-500 text-red-500' : ''
                }`}
              />
              <span className="hidden sm:inline">{isLiked ? likes + 1 : likes}</span>
            </button>
            <span className="flex items-center gap-1 text-xs text-muted-foreground">
              <MessageCircle className="w-4 h-4" />
              <span className="hidden sm:inline">{comments}</span>
            </span>
          </div>
        </div>
      </div>
    </Card>
  )
}
