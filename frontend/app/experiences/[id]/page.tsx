'use client'

import { useState, useEffect } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Card } from '@/components/ui/card'
import { Edit3, Trash2, ArrowLeft, Building2 } from 'lucide-react'
import { api } from '@/lib/api'
import { ExperienceInsightCard } from '@/components/ExperienceInsightCard'
import Link from 'next/link'

interface Experience {
  id: string
  title: string
  content: string
  tags: string[]
  category: string
  score_qualite: number
  sentiment?: string
  date_creation: string
  utilisateur_id: string
  company_name?: string
}

interface Insight {
  experience_id: string
  sentiment: string
  sentiment_label: string
  sentiment_color: string
  keywords: string[]
  confidence: number
  created_at: string
}

export default function ExperienceDetailPage() {
  const params = useParams()
  const router = useRouter()
  const [experience, setExperience] = useState<Experience | null>(null)
  const [insight, setInsight] = useState<Insight | null>(null)
  const [loading, setLoading] = useState(true)
  const [insightLoading, setInsightLoading] = useState(true)
  const [isOwner, setIsOwner] = useState(false)
  const userId = localStorage.getItem('user_id')

  useEffect(() => {
    if (params.id) {
      fetchExperience(params.id as string)
      fetchInsights(params.id as string)
    }
  }, [params.id])

  const fetchInsights = async (id: string) => {
    try {
      setInsightLoading(true)
      const response = await api.get(`experience/${id}/insights`)
      setInsight(response.data)
    } catch (error) {
      console.error('Failed to fetch insights', error)
      // Ne pas bloquer l'affichage si les insights ne sont pas disponibles
    } finally {
      setInsightLoading(false)
    }
  }

  const fetchExperience = async (id: string) => {
    try {
      const response = await api.get(`experience/${id}`)
      const data = response.data
      setExperience({
        ...data,
        tags: data.tags || []
      })
      if (userId) {
        setIsOwner(userId === data.user_id)
      }
    } catch (error) {
      console.error('Failed to fetch experience', error)
    } finally {
      setLoading(false)
    }
  }

  const handleDelete = async () => {
    if (!experience) return
    if (!confirm('Supprimer cette expérience ?')) return
    try {
      await api.delete(`experience/${experience.id}`, {
        headers: { 'x_user_id': userId }
      })
      router.back()
    } catch (error) {
      console.error('Delete failed', error)
    }
  }

  if (loading) return <div className="p-8">Chargement...</div>
  if (!experience) return <div>Expérience non trouvée</div>

  return (
    <main className="min-h-screen bg-background">
      <Navigation />
      <div className="max-w-4xl mx-auto p-8">
        <Button variant="ghost" onClick={() => router.back()} className="mb-6">
          <ArrowLeft className="w-4 h-4 mr-2" />
          Retour
        </Button>

        <Card className="p-8">
          <div className="flex justify-between items-start mb-6">
            <div>
              <h1 className="text-3xl font-bold mb-2">{experience.title}</h1>
              <div className="flex gap-2 items-center mb-2">
                {experience.company_name && (
                  <div className="flex items-center gap-1.5 text-sm text-muted-foreground font-medium">
                    <Building2 className="w-4 h-4" />
                    <span>{experience.company_name}</span>
                  </div>
                )}
                {experience.category && (
                  <Badge variant="outline">{experience.category}</Badge>
                )}
              </div>
            </div>
            {isOwner && (
              <div className="flex gap-2">
                <Button variant="outline" asChild>
                  <Link href={`/experiences/${experience.id}/edit`}>
                    <Edit3 className="w-4 h-4 mr-2" />
                    Modifier
                  </Link>
                </Button>
                <Button variant="destructive" onClick={handleDelete}>
                  <Trash2 className="w-4 h-4 mr-2" />
                  Supprimer
                </Button>
              </div>
            )}
          </div>

          <div className="prose max-w-none mb-8">
            <div dangerouslySetInnerHTML={{ __html: experience.content }} />
          </div>

          {/* Insights IA */}
          {!insightLoading && insight && (
            <div className="mb-8">
              <ExperienceInsightCard
                sentiment={insight.sentiment}
                sentiment_label={insight.sentiment_label}
                sentiment_color={insight.sentiment_color}
                keywords={insight.keywords}
                confidence={insight.confidence}
                created_at={insight.created_at}
              />
            </div>
          )}

          {experience.tags && experience.tags.length > 0 && (
            <div className="mb-6">
              <h3 className="font-semibold mb-3">Tags</h3>
              <div className="flex gap-2 flex-wrap">
                {experience.tags.map((tag) => (
                  <Badge key={tag} variant="secondary">{tag}</Badge>
                ))}
              </div>
            </div>
          )}

          <div className="flex gap-4 text-sm text-muted-foreground">
            <span>Qualité: {experience.score_qualite.toFixed(1)}/10</span>
            <span>Créé le {new Date(experience.date_creation).toLocaleDateString()}</span>
          </div>
        </Card>
      </div>
    </main>
  )
}
