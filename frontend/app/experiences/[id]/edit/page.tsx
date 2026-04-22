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
import { api } from '@/lib/api'

interface ExperienceFormData {
  titre: string
  contenu: string
  tags: string[]
  domaine_activite: string
}

export default function EditExperiencePage() {
  const params = useParams()
  const router = useRouter()
  const [formData, setFormData] = useState<ExperienceFormData>({
    titre: '',
    contenu: '',
    tags: [],
  domaine_activite: ''
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
      const response = await api.get(`/api/experiences/${id}`)
      const data = response.data
      setFormData({
        titre: data.titre,
        contenu: data.contenu,
        tags: data.tags ? data.tags.split(',').map((t: string) => t.trim()).filter(Boolean) : [],
        domaine_activite: data.domaine_activite || ''
      })
      if (userId) {
        setIsOwner(parseInt(userId) === data.utilisateur_id)
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
      await api.put(`/api/experiences/${params.id}`, {
        titre: formData.titre,
        contenu: formData.contenu,
        tags: formData.tags.join(', '),
        domaine_activite: formData.domaine_activite
      }, {
        headers: { 'x_user_id': userId }
      })
      router.push(`/experiences/${params.id}`)
    } catch (error) {
      console.error('Update failed', error)
      alert('Erreur modification')
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
              <Label htmlFor="titre">Titre</Label>
              <Input
                id="titre"
                value={formData.titre}
                onChange={(e) => setFormData({...formData, titre: e.target.value})}
              />
            </div>

            <div>
              <Label htmlFor="contenu">Contenu</Label>
              <RichTextEditor
                value={formData.contenu}
                onChange={(value) => setFormData({...formData, contenu: value})}
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
              <Label htmlFor="domaine">Domaine</Label>
              <Input
                id="domaine"
                value={formData.domaine_activite}
                onChange={(e) => setFormData({...formData, domaine_activite: e.target.value})}
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
