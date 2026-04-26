'use client'

import { useState, useEffect } from 'react'
import { Navigation } from '@/components/Navigation'
import { ExperienceCard } from '@/components/ExperienceCard'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Search, Plus } from 'lucide-react'
import Link from 'next/link'
import { api } from '@/lib/api'

interface Experience {
  id: string
  title: string
  content: string
  tags: string[]
  score_qualite: number
  date_creation: string
  preview: string
  sentiment?: string
  company_name?: string
}

export default function ExperiencesPage() {
  const [experiences, setExperiences] = useState<Experience[]>([])
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState('')

  useEffect(() => {
    fetchExperiences()
  }, [])

  const fetchExperiences = async () => {
    try {
      const userId = localStorage.getItem('user_id')
      if (!userId) throw new Error('User not logged in')
   const response = await api.get('/experience/mes-experiences', {
        headers: { 'x_user_id': userId }
      })
      setExperiences(response.data.map((exp: any) => ({
        ...exp,
        preview: exp.content.slice(0, 200),
        tags: exp.tags || []
      })))
    } catch (error) {
      console.error('Failed to fetch experiences', error)
    } finally {
      setLoading(false)
    }
  }

  const filteredExperiences = experiences.filter(exp =>
    exp.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    exp.content.toLowerCase().includes(searchQuery.toLowerCase())
  )

  if (loading) return <div>Loading...</div>

  return (
    <main className="min-h-screen bg-background">
      <Navigation />
      
        <div className="p-8 max-w-4xl mx-auto space-y-6">
          <div className="flex justify-between items-start">
            <div>
              <h1 className="text-3xl font-bold">Mes Expériences</h1>
              <p className="text-muted-foreground">Vos expériences partagées</p>
            </div>
            <Button asChild>
              <Link href="/experiences/create">
                <Plus className="w-4 h-4 mr-2" />
                Nouvelle expérience
              </Link>
            </Button>
          </div>

          <div className="relative">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input
              placeholder="Rechercher vos expériences..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-12"
            />
          </div>

          <div className="space-y-4">
            {filteredExperiences.length === 0 ? (
              <div className="text-center py-20">
                <p className="text-muted-foreground mb-4">Aucune expérience trouvée.</p>
                <Button asChild>
                  <Link href="/experiences/create">
                    Créer votre première expérience
                  </Link>
                </Button>
              </div>
            ) : (
              filteredExperiences.map((exp) => (
                <Link key={exp.id} href={`/experiences/${exp.id}`} className="block">
                  <ExperienceCard
                    id={exp.id}
                    title={exp.title}
                    preview={exp.preview}
                    author={{ name: 'Vous' }}
                    tags={exp.tags}
                    companyName={exp.company_name}
                    likes={0}
                    comments={0}
                    sentiment={exp.sentiment as any}
                    date="Maintenant"
                  />
                </Link>
              ))
            )}
          </div>
        </div>

    </main>
  )
}
