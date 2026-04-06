'use client'

import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ExperienceCard } from '@/components/ExperienceCard'
import { ArrowLeft, Calendar, MapPin, Users, Share2 } from 'lucide-react'
import Link from 'next/link'
import { use } from 'react'

export default function EventDetailPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = use(params)
  
  const event = {
    id,
    title: 'Tech Summit 2024',
    date: 'April 15, 2024',
    time: '9:00 AM - 6:00 PM',
    location: 'San Francisco, CA',
    category: 'conference',
    description: `The biggest tech conference of the year featuring keynotes from industry leaders, workshops, and networking opportunities. This year's focus is on AI, distributed systems, and career growth in tech.`,
    attendees: 2500,
    relatedExperiences: 145,
    website: 'techsummit2024.com',
  }

  const experiences = [
    {
      id: '1',
      title: 'Great opportunity to network with industry leaders',
      preview:
        'Tech Summit 2024 was an amazing experience with incredible keynotes and networking opportunities.',
      author: { name: 'Sarah Johnson', avatar: undefined },
      tags: ['Networking', 'Learning', 'Industry Event'],
      event: 'Tech Summit 2024',
      likes: 234,
      comments: 45,
      sentiment: 'positive' as const,
      date: '1 day ago',
    },
    {
      id: '2',
      title: 'Learned valuable insights from keynote speakers',
      preview:
        'The keynote speakers at Tech Summit shared valuable insights about the future of AI and distributed systems.',
      author: { name: 'Alex Chen', avatar: undefined },
      tags: ['AI', 'Learning', 'Innovation'],
      likes: 156,
      comments: 28,
      sentiment: 'positive' as const,
      date: '1 day ago',
    },
  ]

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/events" />

      <div className="max-w-3xl mx-auto px-4 py-8 space-y-6">
        {/* Header */}
        <Link href="/events">
          <Button variant="ghost" size="icon" className="rounded-lg mb-4">
            <ArrowLeft className="w-5 h-5" />
          </Button>
        </Link>

        {/* Event Card */}
        <Card className="p-8 space-y-6">
          <div>
            <div className="mb-4">
              <Badge className="capitalize bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300 border-blue-300">
                {event.category}
              </Badge>
            </div>
            <h1 className="text-4xl font-bold text-foreground mb-4 text-balance">
              {event.title}
            </h1>
            <p className="text-lg text-muted-foreground">{event.description}</p>
          </div>

          {/* Event details grid */}
          <div className="grid md:grid-cols-2 gap-4 py-6 border-y border-border">
            <div className="flex items-center gap-3">
              <Calendar className="w-5 h-5 text-accent flex-shrink-0" />
              <div>
                <p className="text-sm text-muted-foreground">Date & Time</p>
                <p className="font-semibold text-foreground">
                  {event.date} · {event.time}
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <MapPin className="w-5 h-5 text-accent flex-shrink-0" />
              <div>
                <p className="text-sm text-muted-foreground">Location</p>
                <p className="font-semibold text-foreground">{event.location}</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <Users className="w-5 h-5 text-accent flex-shrink-0" />
              <div>
                <p className="text-sm text-muted-foreground">Attendees</p>
                <p className="font-semibold text-foreground">
                  {event.attendees.toLocaleString()}
                </p>
              </div>
            </div>

            <div>
              <p className="text-sm text-muted-foreground mb-1">Website</p>
              <a
                href={`https://${event.website}`}
                target="_blank"
                rel="noopener noreferrer"
                className="font-semibold text-primary hover:underline"
              >
                {event.website}
              </a>
            </div>
          </div>

          {/* Actions */}
          <div className="flex gap-3 pt-4">
            <Button className="flex-1 rounded-lg">Register</Button>
            <Button variant="outline" size="icon" className="rounded-lg">
              <Share2 className="w-5 h-5" />
            </Button>
          </div>
        </Card>

        {/* Related experiences */}
        <div className="space-y-4">
          <h2 className="text-2xl font-bold text-foreground">
            Experiences from this event
          </h2>
          <p className="text-muted-foreground">
            {event.relatedExperiences} professionals have shared their
            experiences from {event.title}
          </p>

          {experiences.map((exp) => (
            <Link key={exp.id} href={`/experiences/${exp.id}`}>
              <ExperienceCard {...exp} />
            </Link>
          ))}
        </div>

        {/* Load more */}
        <div className="text-center py-8">
          <Button variant="outline" className="rounded-lg">
            Load More Experiences
          </Button>
        </div>
      </div>
    </main>
  )
}
