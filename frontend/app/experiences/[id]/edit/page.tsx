'use client'

import { useState, useEffect } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card } from '@/components/ui/card'
import { TagInput } from '@/components/TagInput'
import { RichTextEditor } from '@/components/RichTextEditor'
import { CompanySearch } from '@/components/CompanySearch'
import { api } from '@/lib/api'

interface ExperienceFormData {
  title: string
  content: string
  tags: string[]
  category: string
  company_id: string
  event_id: string
}

export default function EditExperiencePage() {
  const params = useParams()
  const router = useRouter()
  const [formData, setFormData] = useState<ExperienceFormData>({
    title: '',
    content: '',
    tags: [],
    category: '',
    company_id: '',
    event_id: ''
  })
  const [loading, setLoading] = useState(false)
  const [isOwner, setIsOwner] = useState(false)
  const userId = localStorage.getItem('user_id')

  useEffect(() => {
    if (params.id) {
      fetchExperience(params.id as string)
    }
  }, [params.id])

  const fetchExperience = async (id: string) => {
    try {
      const response = await api.get(`experience/${id}`)
      const data = response.data
      setFormData({
        title: data.title,
        content: data.content,
        tags: data.tags || [],
        category: data.category || '',
        company_id: data.company_id || '',
        event_id: data.event_id || ''
      })
      if (userId) {
        setIsOwner(userId === data.user_id)
      }
    } catch (error) {
      console.error('Fetch failed', error)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!params.id || !isOwner) return
    setLoading(true)
    try {
      await api.put(`experience/${params.id}`, {
        title: formData.title.trim(),
        content: formData.content.trim(),
        tags: formData.tags,
        category: formData.category.trim() || null,
        company_id: formData.company_id.trim() || null,
        event_id: formData.event_id.trim() || null
      }, {
        headers: { 'x_user_id': userId }
      })
      router.push(`/experiences/${params.id}`)
    } catch (error: any) {
      console.error('Update failed', error)
      const detail = error.response?.data?.detail
      const errorMsg = Array.isArray(detail) 
        ? detail.map((d: any) => `${d.loc.join('.')}: ${d.msg}`).join('\n')
        : detail || 'Erreur lors de la modification'
      alert(errorMsg)
    } finally {
      setLoading(false)
    }
  }

  if (!isOwner) return <div>Accès refusé</div>

  return (
    <main className="min-h-screen bg-background">
      <Navigation />
      <div className="max-w-2xl mx-auto p-8">
        <div className="flex gap-4 mb-6">
          <Button variant="ghost" onClick={() => router.back()}>
            Annuler
          </Button>
        </div>
        <Card className="p-8">
          <h1 className="text-3xl font-bold mb-8">Modifier Expérience</h1>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <Label htmlFor="title">Titre</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(e) => setFormData({...formData, title: e.target.value})}
              />
            </div>

            <div>
              <Label htmlFor="content">Contenu</Label>
              <RichTextEditor
                value={formData.content}
                onChange={(value) => setFormData({...formData, content: value})}
              />
            </div>

            <div>
              <Label>Tags</Label>
              <TagInput
                value={formData.tags}
                onChange={(tags) => setFormData({...formData, tags})}
              />
            </div>

            <div>
              <Label htmlFor="category">Catégorie</Label>
              <Input
                id="category"
                value={formData.category}
                onChange={(e) => setFormData({...formData, category: e.target.value})}
              />
            </div>

            <div>
              <Label htmlFor="company_id">Entreprise (optionnel)</Label>
              <CompanySearch
                value={formData.company_id}
                onSelect={(id) => setFormData({...formData, company_id: id})}
                placeholder="Ex: Capgemini, Google, etc."
              />
            </div>

            <div>
              <Label htmlFor="event_id">ID Événement (optionnel)</Label>
              <Input
                id="event_id"
                value={formData.event_id}
                onChange={(e) => setFormData({...formData, event_id: e.target.value})}
                placeholder="UUID de l'événement"
              />
            </div>

            <Button type="submit" className="w-full" disabled={loading}>
              {loading ? 'Sauvegarde...' : 'Mettre à jour'}
            </Button>
          </form>
        </Card>
      </div>
    </main>
  )
}
