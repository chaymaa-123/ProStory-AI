'use client'

import { Navigation } from '@/components/Navigation'
import { Sidebar } from '@/components/Sidebar'
import { ExperienceCard } from '@/components/ExperienceCard'
import { QuickExperienceModal } from '@/components/QuickExperienceModal'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Search, Plus } from 'lucide-react'
import Link from 'next/link'
import { useState, useMemo } from 'react'

// Mock data
const mockExperiences = [
  {
    id: '1',
    title: 'Amazing culture at Tech Corp - Everyone is respected and valued',
    preview:
      'I have been working at Tech Corp for 3 years and the culture has been consistently amazing. The leadership genuinely cares about employee development and work-life balance.',
    author: {
      name: 'Sarah Johnson',
      avatar: undefined,
    },
    tags: ['Company Culture', 'Remote Work', 'Career Growth'],
    event: 'Tech Summit 2024',
    likes: 145,
    comments: 23,
    sentiment: 'positive' as const,
    date: '2 days ago',
  },
  {
    id: '2',
    title: 'Great opportunity for learning and growth',
    preview:
      'Started as a junior developer and within 6 months I was leading a team. The mentorship here is exceptional and the learning opportunities are endless.',
    author: {
      name: 'Alex Chen',
      avatar: undefined,
    },
    tags: ['Career Growth', 'Team Leadership', 'Professional Development'],
    likes: 89,
    comments: 12,
    sentiment: 'positive' as const,
    date: '4 days ago',
  },
  {
    id: '3',
    title: 'Challenging work environment with unclear communication',
    preview:
      'While the projects are interesting, the lack of clear communication between teams makes it difficult to succeed. Process improvements needed.',
    author: {
      name: 'Jordan Smith',
      avatar: undefined,
    },
    tags: ['Communication', 'Team Leadership', 'Process'],
    likes: 56,
    comments: 8,
    sentiment: 'negative' as const,
    date: '5 days ago',
  },
  {
    id: '4',
    title: 'Neutral experience - average corporate environment',
    preview:
      'Nothing particularly exceptional, but also nothing problematic. Standard corporate policies and benefits. Good for a stable job.',
    author: {
      name: 'Morgan Lee',
      avatar: undefined,
    },
    tags: ['Work Environment', 'Stability'],
    likes: 34,
    comments: 5,
    sentiment: 'neutral' as const,
    date: '6 days ago',
  },
  {
    id: '5',
    title: 'Innovation is at the heart of everything we do',
    preview:
      'Being part of a company that pushes boundaries and encourages creative thinking is incredibly fulfilling. Every idea is valued.',
    author: {
      name: 'Casey Brown',
      avatar: undefined,
    },
    tags: ['Innovation', 'Company Culture', 'Remote Work'],
    event: 'Leadership Workshop',
    likes: 234,
    comments: 45,
    sentiment: 'positive' as const,
    date: '1 week ago',
  },
]

export default function FeedPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [isModalOpen, setIsModalOpen] = useState(false)

  const filteredExperiences = useMemo(() => {
    return mockExperiences.filter((exp) => {
      const matchesSearch =
        searchQuery === '' ||
        exp.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        exp.preview.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (exp.tags && exp.tags.some((tag) =>
          tag.toLowerCase().includes(searchQuery.toLowerCase())
        ))

      return matchesSearch
    })
  }, [searchQuery])

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation currentPath="/feed" />

      <div className="flex-1 flex overflow-hidden">
        {/* Main content */}
        <div className="flex-1 border-r border-border overflow-y-auto">
          <div className="max-w-3xl mx-auto w-full px-4 md:px-6 py-6 md:py-8 space-y-6">
            {/* Header with search and filter */}
            <div className="sticky top-0 bg-background/95 backdrop-blur-sm pt-4 pb-6 -mx-4 md:-mx-6 px-4 md:px-6 space-y-4 border-b border-border z-10">
              <div className="flex items-center justify-between gap-4">
                <h1 className="text-2xl md:text-3xl font-bold text-foreground">Expériences</h1>
                <Button 
                  size="sm" 
                  className="rounded-lg shrink-0"
                  onClick={() => setIsModalOpen(true)}
                >
                  <Plus className="w-4 h-4 mr-2" />
                  <span className="hidden sm:inline">Partager</span>
                </Button>
              </div>

              {/* Search */}
              <div className="relative">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-muted-foreground" />
                <Input
                  placeholder="Chercher expériences, tags..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="pl-10 py-2 rounded-lg text-sm md:text-base"
                />
              </div>
            </div>

            {/* Experiences list */}
            <div className="space-y-4 pb-8">
              {filteredExperiences && filteredExperiences.length > 0 ? (
                filteredExperiences.map((exp) => (
                  <div key={exp.id} className="block hover:opacity-95 transition-opacity cursor-pointer">
                    <ExperienceCard {...exp} />
                  </div>
                ))
              ) : (
                <div className="text-center py-16">
                  <p className="text-muted-foreground text-base">
                    Aucune expérience trouvée. Ajustez vos filtres.
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <aside className="hidden lg:block w-72 xl:w-80 border-l border-border overflow-y-auto">
          <div className="sticky top-0 h-screen overflow-y-auto">
            <Sidebar />
          </div>
        </aside>
      </div>

      {/* Quick Experience Modal */}
      <QuickExperienceModal
        open={isModalOpen}
        onOpenChange={setIsModalOpen}
        onSubmit={(data) => {
          console.log('New experience:', data)
          // Here you would add the experience to the list
        }}
      />
    </div>
  )
}
