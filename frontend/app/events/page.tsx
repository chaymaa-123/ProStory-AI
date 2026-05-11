'use client'

import { Navigation } from '@/components/Navigation'
import { EventCard } from '@/components/EventCard'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Search, Plus, Loader2, Calendar } from 'lucide-react'
import { useState, useEffect, useMemo } from 'react'
import Link from 'next/link'

// ── Événements maquettes à venir (TechNova Solutions + EcoFuture Group) ────────
// Ces données sont utilisées comme fallback si l'API n'est pas disponible.
// Les "vrais" événements seront insérés en DB via scripts/setup_enterprise_accounts.py
const MOCK_EVENTS = [
  // ── TechNova Solutions ──────────────────────────────────────────────────────
  {
    id:                 'tn-1',
    title:              'Tech Summit 2026 – Casablanca',
    date:               '28 mai 2026',
    time:               '9:00',
    location:           'Casablanca, Maroc',
    category:           'Technologie',
    description:        'Le plus grand rassemblement d\'innovation tech de la région MENA. Keynotes, ateliers pratiques et networking intensif.',
    attendees:          1500,
    relatedExperiences: 0,
    company:            'TechNova Solutions',
  },
  {
    id:                 'tn-2',
    title:              'AI & Data Day – Rabat',
    date:               '18 juin 2026',
    time:               '10:00',
    location:           'Rabat, Maroc',
    category:           'Technologie',
    description:        'Journée dédiée à l\'intelligence artificielle et la data science. Découvrez les tendances, les outils et les cas d\'usage concrets.',
    attendees:          500,
    relatedExperiences: 0,
    company:            'TechNova Solutions',
  },
  {
    id:                 'tn-3',
    title:              'Hackathon Innovation 2026',
    date:               '12 juillet 2026',
    time:               '8:00',
    location:           'Casablanca, Maroc',
    category:           'Technologie',
    description:        '48h pour concevoir des solutions tech innovantes. Équipes de 3 à 5 personnes — des prizes attractifs à la clé.',
    attendees:          300,
    relatedExperiences: 0,
    company:            'TechNova Solutions',
  },
  // ── EcoFuture Group ─────────────────────────────────────────────────────────
  {
    id:                 'ef-1',
    title:              'Webinar – Bâtiments à énergie positive',
    date:               '22 mai 2026',
    time:               '14:00',
    location:           'En ligne',
    category:           'Environnement',
    description:        'Découvrez comment concevoir des bâtiments qui produisent plus d\'énergie qu\'ils n\'en consomment. Inscription gratuite.',
    attendees:          1000,
    relatedExperiences: 0,
    company:            'EcoFuture Group',
  },
  {
    id:                 'ef-2',
    title:              'Sustainability Week 2026',
    date:               '10 juin 2026',
    time:               '9:00',
    location:           'Rabat, Maroc',
    category:           'Environnement',
    description:        'Une semaine dédiée aux énergies propres, au développement durable et aux solutions climatiques innovantes.',
    attendees:          800,
    relatedExperiences: 0,
    company:            'EcoFuture Group',
  },
  {
    id:                 'ef-3',
    title:              'Green Energy Forum',
    date:               '5 juillet 2026',
    time:               '10:00',
    location:           'Marrakech, Maroc',
    category:           'Environnement',
    description:        'Forum international sur les énergies renouvelables — solaire, éolien, hydrogène vert. Experts du monde entier.',
    attendees:          600,
    relatedExperiences: 0,
    company:            'EcoFuture Group',
  },
]

const ALL_CATEGORIES = ['Technologie', 'Environnement', 'Management', 'Carrière', 'Santé']

type EventItem = typeof MOCK_EVENTS[0]

export default function EventsPage() {
  const [searchQuery,       setSearchQuery]       = useState('')
  const [selectedCategory,  setSelectedCategory]  = useState<string | null>(null)
  const [selectedCompany,   setSelectedCompany]   = useState<string | null>(null)
  const [events,            setEvents]            = useState<EventItem[]>(MOCK_EVENTS)
  const [isLoading,         setIsLoading]         = useState(true)

  // Fetch depuis l'API, fallback sur les mocks
  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const res = await fetch(
          `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'}/events/upcoming?limit=20`
        )
        if (!res.ok) throw new Error('API error')
        const data = await res.json()

        if (Array.isArray(data) && data.length > 0) {
          // Transformer le format API vers le format interne
          const formatted: EventItem[] = data.map((evt: any) => ({
            id:                 evt.id,
            title:              evt.title,
            date:               new Date(evt.date).toLocaleDateString('fr-FR', {
                                  day: 'numeric', month: 'long', year: 'numeric'
                                }),
            time:               new Date(evt.date).toLocaleTimeString('fr-FR', {
                                  hour: '2-digit', minute: '2-digit'
                                }),
            location:           evt.location || 'À définir',
            category:           evt.category || 'Autre',
            description:        evt.description || '',
            attendees:          evt.max_attendees || 0,
            relatedExperiences: 0,
            company:            evt.company_name || '',
          }))
          setEvents(formatted)
        }
      } catch {
        // On garde les mocks
      } finally {
        setIsLoading(false)
      }
    }
    fetchEvents()
  }, [])

  const companies = useMemo(() => {
    const names = events.map((e) => e.company).filter(Boolean)
    return [...new Set(names)]
  }, [events])

  const filteredEvents = useMemo(() => {
    return events.filter((event) => {
      const matchesSearch =
        searchQuery === '' ||
        event.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        event.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (event.company && event.company.toLowerCase().includes(searchQuery.toLowerCase()))

      const matchesCategory = !selectedCategory || event.category === selectedCategory
      const matchesCompany  = !selectedCompany  || event.company  === selectedCompany

      return matchesSearch && matchesCategory && matchesCompany
    })
  }, [events, searchQuery, selectedCategory, selectedCompany])

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/events" />

      <div className="max-w-7xl mx-auto px-4 py-8 space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-1 flex items-center gap-2">
              <Calendar className="w-8 h-8 text-accent" />
              Événements à venir
            </h1>
            <p className="text-muted-foreground text-sm">
              Découvrez les prochains événements de <strong>TechNova Solutions</strong> et{' '}
              <strong>EcoFuture Group</strong>
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
            placeholder="Chercher un événement, une entreprise..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-10 rounded-lg"
          />
        </div>

        {/* Filters row */}
        <div className="flex flex-wrap gap-2">
          {/* All */}
          <button
            onClick={() => { setSelectedCategory(null); setSelectedCompany(null) }}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              !selectedCategory && !selectedCompany
                ? 'bg-primary text-primary-foreground'
                : 'bg-muted text-muted-foreground hover:bg-muted/80'
            }`}
          >
            Tous
          </button>

          {/* Category filters */}
          {ALL_CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => { setSelectedCategory(cat); setSelectedCompany(null) }}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                selectedCategory === cat
                  ? 'bg-primary text-primary-foreground'
                  : 'bg-muted text-muted-foreground hover:bg-muted/80'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Company filters */}
        {companies.length > 0 && (
          <div className="flex flex-wrap gap-2">
            <span className="text-xs text-muted-foreground self-center mr-1">Entreprise :</span>
            {companies.map((comp) => (
              <button
                key={comp}
                onClick={() => {
                  setSelectedCompany(selectedCompany === comp ? null : comp)
                  setSelectedCategory(null)
                }}
                className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-colors ${
                  selectedCompany === comp
                    ? 'bg-accent text-white border-accent'
                    : 'bg-muted text-muted-foreground border-border hover:border-accent/50'
                }`}
              >
                {comp}
              </button>
            ))}
          </div>
        )}

        {/* Events grid */}
        {isLoading ? (
          <div className="flex justify-center py-20">
            <Loader2 className="w-8 h-8 animate-spin text-primary" />
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredEvents.length > 0 ? (
              filteredEvents.map((event) => (
                <Link key={event.id} href={`/events/${event.id}`}>
                  <EventCard
                    id={event.id}
                    title={event.title}
                    date={event.date}
                    time={event.time}
                    location={event.location}
                    category={event.category}
                    description={event.description}
                    attendees={event.attendees}
                    relatedExperiences={event.relatedExperiences}
                  />
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
        )}
      </div>
    </main>
  )
}
