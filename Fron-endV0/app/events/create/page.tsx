'use client'

import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { ArrowLeft, Calendar, MapPin, Users } from 'lucide-react'
import Link from 'next/link'
import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function CreateEventPage() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    date: '',
    location: '',
    maxAttendees: '',
  })
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)

    // Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 500))

    // Navigate to events page
    router.push('/events')
  }

  return (
    <div className="min-h-screen flex flex-col bg-background">
      <Navigation currentPath="/events" />

      <div className="flex-1 flex items-center justify-center px-4 py-12">
        <div className="w-full max-w-2xl">
          {/* Header */}
          <div className="mb-8">
            <Link href="/events" className="inline-flex items-center gap-2 text-primary hover:underline text-sm font-medium mb-4">
              <ArrowLeft className="w-4 h-4" />
              Retour aux événements
            </Link>
            <h1 className="text-3xl font-bold text-foreground mb-2">Créer un événement</h1>
            <p className="text-muted-foreground">Organize your next networking event and let people share their experiences</p>
          </div>

          <Card className="p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Title */}
              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  Titre de l&apos;événement
                </label>
                <Input
                  type="text"
                  name="title"
                  placeholder="Tech Summit 2024, Team Dinner, Conference..."
                  value={formData.title}
                  onChange={handleChange}
                  required
                  className="rounded-lg"
                />
              </div>

              {/* Description */}
              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  Description
                </label>
                <Textarea
                  name="description"
                  placeholder="Décris l'événement, ce qui va se passer, pourquoi c'est important..."
                  value={formData.description}
                  onChange={handleChange}
                  rows={4}
                  className="rounded-lg resize-none"
                />
              </div>

              {/* Date */}
              <div>
                <label className="block text-sm font-medium text-foreground mb-2 flex items-center gap-2">
                  <Calendar className="w-4 h-4" />
                  Date de l&apos;événement
                </label>
                <Input
                  type="datetime-local"
                  name="date"
                  value={formData.date}
                  onChange={handleChange}
                  required
                  className="rounded-lg"
                />
              </div>

              {/* Location */}
              <div>
                <label className="block text-sm font-medium text-foreground mb-2 flex items-center gap-2">
                  <MapPin className="w-4 h-4" />
                  Lieu
                </label>
                <Input
                  type="text"
                  name="location"
                  placeholder="Paris, France / Online / HQ Office..."
                  value={formData.location}
                  onChange={handleChange}
                  required
                  className="rounded-lg"
                />
              </div>

              {/* Max Attendees */}
              <div>
                <label className="block text-sm font-medium text-foreground mb-2 flex items-center gap-2">
                  <Users className="w-4 h-4" />
                  Nombre max de participants (optionnel)
                </label>
                <Input
                  type="number"
                  name="maxAttendees"
                  placeholder="50, 100, 500..."
                  value={formData.maxAttendees}
                  onChange={handleChange}
                  className="rounded-lg"
                />
              </div>

              {/* Actions */}
              <div className="flex gap-3 pt-4 border-t border-border">
                <Link href="/events" className="flex-1">
                  <Button
                    type="button"
                    variant="outline"
                    className="w-full rounded-lg"
                  >
                    Annuler
                  </Button>
                </Link>
                <Button
                  type="submit"
                  className="flex-1 rounded-lg"
                  disabled={isSubmitting}
                >
                  {isSubmitting ? 'Création...' : 'Créer l\'événement'}
                </Button>
              </div>
            </form>
          </Card>
        </div>
      </div>
    </div>
  )
}
