'use client'

import { Navigation } from '@/components/Navigation'
import { Sidebar } from '@/components/Sidebar'
import { ExperienceCard } from '@/components/ExperienceCard'
import { QuickExperienceModal } from '@/components/QuickExperienceModal'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Search, Plus, Loader2 } from 'lucide-react'
import { useState, useMemo, useEffect } from 'react'
import { experienceApi } from '@/lib/api'

export default function FeedPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [experiences, setExperiences] = useState<any[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // Fetch experiences from API
  const fetchExperiences = async () => {
    setIsLoading(true)
    setError(null)
    try {
      const response = await experienceApi.feed()
      setExperiences(response.data)
    } catch (err) {
      console.error('Failed to fetch experiences:', err)
      setError('Impossible de charger les experiences. Veuillez reessayer.')
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    fetchExperiences()
  }, [])

  const filteredExperiences = useMemo(() => {
    if (!experiences) return []
    return experiences.filter((exp) => {
      const matchesSearch =
        searchQuery === '' ||
        exp.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        exp.content.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (exp.tags && exp.tags.some((tag: string) =>
          tag.toLowerCase().includes(searchQuery.toLowerCase())
        )) ||
        (exp.company_name && exp.company_name.toLowerCase().includes(searchQuery.toLowerCase())) ||
        (exp.author_name && exp.author_name.toLowerCase().includes(searchQuery.toLowerCase()))

      return matchesSearch
    })
  }, [searchQuery, experiences])

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
                <h1 className="text-2xl md:text-3xl font-bold text-foreground">Experiences</h1>
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
                  placeholder="Chercher experiences, tags, entreprises..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="pl-10 py-2 rounded-lg text-sm md:text-base"
                />
              </div>
            </div>

            {/* Experiences list */}
            <div className="space-y-4 pb-8">
              {isLoading ? (
                <div className="flex flex-col items-center justify-center py-20 space-y-4">
                  <Loader2 className="w-8 h-8 text-primary animate-spin" />
                  <p className="text-sm text-muted-foreground">Chargement des experiences...</p>
                </div>
              ) : error ? (
                <div className="text-center py-20">
                  <p className="text-red-500 mb-4">{error}</p>
                  <Button onClick={fetchExperiences} variant="outline">Reessayer</Button>
                </div>
              ) : filteredExperiences.length > 0 ? (
                filteredExperiences.map((exp) => (
                  <div key={exp.id} className="block hover:opacity-95 transition-opacity cursor-pointer">
                    <ExperienceCard 
                      id={exp.id}
                      title={exp.title}
                      preview={exp.content}
                      author={{ name: exp.author_name || 'Anonyme' }}
                      tags={exp.tags || []}
                      companyName={exp.company_name}
                      event={exp.event_name}
                      likes={0}
                      comments={0}
                      date={new Date(exp.created_at).toLocaleDateString('fr-FR', {
                        day: 'numeric',
                        month: 'short',
                        year: 'numeric'
                      })}
                    />
                  </div>
                ))
              ) : (
                <div className="text-center py-16">
                  <p className="text-muted-foreground text-base">
                    Aucune experience trouvee. Soyez le premier a partager !
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
        onSubmit={() => {
          fetchExperiences()
          setIsModalOpen(false)
        }}
      />
    </div>
  )
}
