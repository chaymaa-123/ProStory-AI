'use client'

import { Navigation } from '@/components/Navigation'
import { EventCard } from '@/components/EventCard'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Search, Plus } from 'lucide-react'
import { useState } from 'react'
import Link from 'next/link'

// Mock data
const mockEvents = [
  {
    id: '1',
    title: 'Tech Summit 2024',
    date: 'Apr 15, 2024',
    time: '9:00 AM',
    location: 'San Francisco, CA',
    category: 'conference',
    description:
      'The biggest tech conference of the year featuring keynotes from industry leaders.',
    attendees: 2500,
    relatedExperiences: 145,
  },
  {
    id: '2',
    title: 'Leadership Workshop',
    date: 'Apr 18, 2024',
    time: '2:00 PM',
    location: 'Virtual',
    category: 'workshop',
    description: 'Interactive workshop on modern leadership practices and team dynamics.',
    attendees: 300,
    relatedExperiences: 42,
  },
  {
    id: '3',
    title: 'Career Growth Webinar',
    date: 'Apr 22, 2024',
    time: '1:00 PM',
    location: 'Virtual',
    category: 'webinar',
    description: 'Expert panel discussing career advancement strategies in tech.',
    attendees: 800,
    relatedExperiences: 67,
  },
  {
    id: '4',
    title: 'Industry Meetup',
    date: 'Apr 25, 2024',
    time: '6:00 PM',
    location: 'New York, NY',
    category: 'meetup',
    description: 'Casual networking event for professionals in the tech industry.',
    attendees: 150,
    relatedExperiences: 23,
  },
  {
    id: '5',
    title: 'Product Management Conference',
    date: 'May 1, 2024',
    time: '8:00 AM',
    location: 'Austin, TX',
    category: 'conference',
    description:
      'Deep dive into product management trends, tools, and best practices.',
    attendees: 1200,
    relatedExperiences: 89,
  },
  {
    id: '6',
    title: 'Frontend Development Masterclass',
    date: 'May 5, 2024',
    time: '10:00 AM',
    location: 'Virtual',
    category: 'workshop',
    description: 'Learn advanced frontend development techniques from experts.',
    attendees: 500,
    relatedExperiences: 34,
  },
]

export default function EventsPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)

  const categories = ['conference', 'workshop', 'webinar', 'meetup']

  const filteredEvents = mockEvents.filter((event) => {
    const matchesSearch =
      searchQuery === '' ||
      event.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      event.description.toLowerCase().includes(searchQuery.toLowerCase())

    const matchesCategory = !selectedCategory || event.category === selectedCategory

    return matchesSearch && matchesCategory
  })

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/events" />

      <div className="max-w-7xl mx-auto px-4 py-8 space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">Événements</h1>
            <p className="text-muted-foreground">
              Découvre des événements pro et connecte-toi avec des gens
            </p>
          </div>
          <Link href="/events/create">
            <Button className="rounded-lg">
              <Plus className="w-4 h-4 mr-2" />
              Créer un événement
            </Button>
          </Link>
        </div>

        {/* Search */}
        <div className="relative">
          <Search className="absolute left-3 top-3 w-5 h-5 text-muted-foreground" />
          <Input
            placeholder="Chercher un événement..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-10 rounded-lg"
          />
        </div>

        {/* Category filter */}
        <div className="flex gap-2 flex-wrap">
          <button
            onClick={() => setSelectedCategory(null)}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              selectedCategory === null
                ? 'bg-primary text-primary-foreground'
                : 'bg-muted text-muted-foreground hover:bg-muted/80'
            }`}
          >
            Tous les événements
          </button>
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors capitalize ${
                selectedCategory === category
                  ? 'bg-primary text-primary-foreground'
                  : 'bg-muted text-muted-foreground hover:bg-muted/80'
              }`}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Events grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredEvents.length > 0 ? (
            filteredEvents.map((event) => (
              <Link key={event.id} href={`/events/${event.id}`}>
                <EventCard {...event} />
              </Link>
            ))
          ) : (
            <div className="col-span-full text-center py-12">
              <p className="text-muted-foreground">
                Aucun événement trouvé. Ajuste tes filtres.
              </p>
            </div>
          )}
        </div>
      </div>
    </main>
  )
}
