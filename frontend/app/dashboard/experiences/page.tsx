'use client'

import { Navigation } from '@/components/Navigation'
import { DashboardLayout } from '@/components/DashboardLayout'
import { ExperienceCard } from '@/components/ExperienceCard'
import { Input } from '@/components/ui/input'
import { Search } from 'lucide-react'
import { useState } from 'react'
import Link from 'next/link'


const companyExperiences = [
  {
    id: '1',
    title: 'Amazing culture at Tech Corp - Everyone is respected and valued',
    preview:
      'I have been working at Tech Corp for 3 years and the culture has been consistently amazing.',
    author: { name: 'Sarah Johnson', avatar: undefined },
    tags: ['Company Culture', 'Remote Work', 'Career Growth'],
    event: 'Tech Summit 2024',
    likes: 145,
    comments: 23,
    sentiment: 'positive' as const,
    date: '2 days ago',
  },
  {
    id: '2',
    title: 'Challenging work environment at Tech Corp',
    preview:
      'While the projects are interesting, the lack of clear communication between teams makes it difficult.',
    author: { name: 'Jordan Smith', avatar: undefined },
    tags: ['Communication', 'Process'],
    likes: 56,
    comments: 8,
    sentiment: 'negative' as const,
    date: '5 days ago',
  },
  {
    id: '3',
    title: 'Great learning opportunity at Tech Corp',
    preview:
      'Started as a junior at Tech Corp and within 6 months I was leading a team.',
    author: { name: 'Alex Chen', avatar: undefined },
    tags: ['Career Growth', 'Team Leadership'],
    likes: 89,
    comments: 12,
    sentiment: 'positive' as const,
    date: '4 days ago',
  },
]

export default function DashboardExperiencesPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedSentiment, setSelectedSentiment] = useState<
    'all' | 'positive' | 'neutral' | 'negative'
  >('all')

  const filteredExperiences = companyExperiences.filter((exp) => {
    const matchesSearch =
      searchQuery === '' ||
      exp.title.toLowerCase().includes(searchQuery.toLowerCase())

    const matchesSentiment =
      selectedSentiment === 'all' || exp.sentiment === selectedSentiment

    return matchesSearch && matchesSentiment
  })

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/dashboard" />

      <DashboardLayout currentSection="experiences">
        <div className="p-8 max-w-3xl space-y-6">
          {/* Header */}
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">
              Experiences
            </h1>
            <p className="text-muted-foreground">
              All experiences mentioning your company
            </p>
          </div>

          {/* Search */}
          <div className="relative">
            <Search className="absolute left-3 top-3 w-5 h-5 text-muted-foreground" />
            <Input
              placeholder="Search experiences..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 rounded-lg"
            />
          </div>

          {/* Sentiment filter */}
          <div className="flex gap-2 flex-wrap">
            {[
              { value: 'all', label: 'All' },
              { value: 'positive', label: 'Positive' },
              { value: 'neutral', label: 'Neutral' },
              { value: 'negative', label: 'Negative' },
            ].map((option) => (
              <button
                key={option.value}
                onClick={() =>
                  setSelectedSentiment(option.value as typeof selectedSentiment)
                }
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  selectedSentiment === option.value
                    ? 'bg-primary text-primary-foreground'
                    : 'bg-muted text-muted-foreground hover:bg-muted/80'
                }`}
              >
                {option.label}
              </button>
            ))}
          </div>

          {/* Experiences list */}
          <div className="space-y-4">
            {filteredExperiences.length > 0 ? (
              filteredExperiences.map((exp) => (
                <Link key={exp.id} href={`/experiences/${exp.id}`}>
                  <ExperienceCard {...exp} />
                </Link>
              ))
            ) : (
              <div className="text-center py-12 text-muted-foreground">
                <p>No experiences found matching your criteria.</p>
              </div>
            )}
          </div>

          {/* Pagination would go here */}
          {filteredExperiences.length > 10 && (
            <div className="flex items-center justify-center gap-2 mt-8">
              <button className="px-4 py-2 rounded-lg border border-border text-foreground hover:bg-muted">
                ← Previous
              </button>
              <span className="text-sm text-muted-foreground">
                Page 1 of 3
              </span>
              <button className="px-4 py-2 rounded-lg border border-border text-foreground hover:bg-muted">
                Next →
              </button>
            </div>
          )}
        </div>
      </DashboardLayout>
    </main>
  )
}
