'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card } from '@/components/ui/card'
import { Textarea } from '@/components/ui/textarea'
import { TagInput } from '@/components/TagInput'
import { RichTextEditor } from '@/components/RichTextEditor'
import { CompanySearch } from '@/components/CompanySearch'
import { api } from '@/lib/api'

export default function CreateExperiencePage() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    tags: [] as string[],
    category: '',
    company_id: '',
    event_id: ''
  })
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    // Validation locale
    if (formData.title.trim().length < 3) {
      alert('Le titre doit faire au moins 3 caractères')
      return
    }
    if (formData.content.trim().length < 10) {
      alert('Le contenu doit faire au moins 10 caractères')
      return
    }

    setLoading(true)
    try {
      const userId = localStorage.getItem('user_id')
      if (!userId) throw new Error('Utilisateur non connecté')

      const payload = {
        title: formData.title.trim(),
        content: formData.content.trim(),
        tags: formData.tags,
        category: formData.category.trim() || null,
        company_id: formData.company_id.trim() || null,
        event_id: formData.event_id.trim() || null
      }

      // Utilisation du chemin exact avec slash final car le backend utilise @router.post("/")
      await api.post('experience/', payload, {
        headers: { 'x_user_id': userId }
      })
      router.push('/experiences')
    } catch (error: any) {
      console.error('Erreur création', error)
      const detail = error.response?.data?.detail
      const errorMsg = Array.isArray(detail) 
        ? detail.map((d: any) => `${d.loc.join('.')}: ${d.msg}`).join('\n')
        : detail || 'Erreur lors de la création'
      alert(errorMsg)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-background">
      <Navigation />
      <div className="max-w-2xl mx-auto p-8">
        <Button variant="ghost" onClick={() => router.back()} className="mb-6">
          Annuler
        </Button>
        <Card className="p-8">
          <h1 className="text-3xl font-bold mb-8">Nouvelle Expérience</h1>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <Label htmlFor="title">Titre</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(e) => setFormData({...formData, title: e.target.value})}
                placeholder="Titre de votre expérience"
                required
              />
            </div>

            <div>
              <Label htmlFor="content">Contenu</Label>
              <RichTextEditor
                value={formData.content}
                onChange={(value) => setFormData({...formData, content: value})}
                placeholder="Racontez votre expérience..."
              />
            </div>

            <div>
              <Label>Tags</Label>
              <TagInput
                value={formData.tags}
                onChange={(tags) => setFormData({...formData, tags})}
                placeholder="Ajoutez des tags (ex: #startup, #leadership)"
              />
            </div>

            <div>
              <Label htmlFor="category">Catégorie</Label>
              <Input
                id="category"
                value={formData.category}
                onChange={(e) => setFormData({...formData, category: e.target.value})}
                placeholder="Ex: Tech, Marketing, Finance"
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
              {loading ? 'Création...' : 'Publier l\'expérience'}
            </Button>
          </form>
        </Card>
      </div>
    </main>
  )
}
